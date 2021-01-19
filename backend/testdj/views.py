import redis
import json
import re
from django.shortcuts import render, get_object_or_404
import os
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

import requests
from django.http import FileResponse
from ScienceSearcher.SearchEngine import SearchEngine
import fitz



public_url = 'xxx.xxx.xxx.xxx:xxx/' # 本地服务器路径及端口

public_path = '/xx/' # 本地存放论文文件的路径

se = SearchEngine(download_server_ip='xxx.xxx.xxx.xxx',
                  download_server_port=5000,
                  download_client_ip='xxx.xxx.xxx.xxx',
                  download_client_port=9001,
                  es_ip='xxx.xxx.xxx.xxx',
                  es_port=9200,
                  index_name='xxx',
                  video_index_name='xxx',
                  group_name='xxx')

main_rds = redis.StrictRedis(host='localhost', port=6379, db=0, password='')


def detail(request):
    id = int(request.GET.get('id'))
    main_rds.zincrby('hot_hll', 1, id)
    # data = get_detail(id)
    data = se.search_by_id(id)
    # data = eval(data)

    if not os.path.exists(public_path+'imgs/' + str(id) + '.png') and '/' in data['pdfPath']:
        pyMuPDF_fitz(data['pdfPath'],
                    public_path+'imgs/' + str(id) + '.png')
    # print(data['pdfPath'])
    pdfName = '-'.join(data['pdfPath'].split('/')[-3:])
    videoName = '-'.join(data['videoPath'].split('/')[-3:])
    if '/' not in data['pdfPath']:
        data['pdfPath']=''
    else:
        data['pdfPath'] = public_url +'pdf/'+ pdfName
    if '/' not in data['videoPath']:
        data['videoPath']=''
    else:
        data['videoPath'] = public_url +'video/' + videoName
    data = json.dumps(data)
    return HttpResponse(data)


def hot(request):
    num = int(request.GET.get('num'))
    if not num:
        num = 5
    if num < 0:
        return HttpResponse('Error! num can not < 1')
    hot_list = main_rds.zrevrange('hot_hll', 0, num - 1, withscores=False)
    data = []
    for id in hot_list:
        t={}
        id = id.decode()
        t['id']=id
        if se.search_by_id(id):
            t['title'] = se.search_by_id(id)['title']
            t['image'] = public_url + 'img/' + str(id) + '.png'
        else:
            t['title'] = ''
            t['image'] = ''
        data.append(t)
        # imgList.append('W:/web/testdj/testdj/static/img/' + str(id.decode()) + '.img')
    data = json.dumps(data)

    # file = open('W:/web/testdj/testdj/static/img/t.png', 'rb')
    # return HttpResponse(content=file.read(),
    #                     content_type='img/jpeg')
    return HttpResponse(data)


def image(request, name):
    try:
        file = open(public_path+'imgs/' + name, 'rb')
    except FileNotFoundError:
        file = open(public_path+'imgs/0.png', 'rb')
    return HttpResponse(content=file.read(),
                        content_type='img/jpeg')


def pdf(request, name):
    try:
        # print("!!!!!!"+name)
        name=name.replace('-','/')
        # print("!!!!!!" + name)
        file = open(public_path + name, 'rb')
    except FileNotFoundError:
        return HttpResponse('Pdf in not Exist!!')
    return HttpResponse(content=file.read(),
                        content_type='application/pdf')

def video(request, name):
    try:
        name = name.replace('-', '/')
        # print(name)
        file = open(public_path + name, 'rb')
    except FileNotFoundError:
        return HttpResponse('Video in not Exist!!')
    return HttpResponse(content=file.read(),
                        content_type='application/video')

def results(request):
    # from ScienceSearcher.SearchEngine import SearchEngine

    # initialization
    # se = SearchEngine(download_server_ip='xxx.xxx.xxx.xxx',
    #                   download_server_port=5000,
    #                   download_client_ip='xxx.xxx.xxx.xxx',
    #                   download_client_port=9001,
    #                   es_ip='xxx.xxx.xxx.xxx',
    #                   es_port=9200,
    #                   index_name='xxx',
    #                   video_index_name='xxx',
    #                   group_name='xxx')

    # GET type and query
    type1 = int(request.GET.get('type'))
    q = request.GET.get('query')
    # generate dict
    query = {'top_number': 200}  # 返回论文数量
    if int(type1) == 1:
        # 后端测试使用q
        # q = {
        #     "title": "GNN",
        #     "author": "Hinton",
        #     "abstract": "",
        #     "content": "this paper proposed",
        #     "operator": ["OR", "AND", "", "NOT"],
        # }
        q=eval(q)
        operator = q["operator"]
        q.pop("operator")
        query["type"] = int(type1)
        query["query_text"] = q
        query["operator"] = operator
    else:
        query["type"] = int(type1)
        query["query_text"] = q

    # 测试使用
    # papers = searchpapers(query)
    # 正式使用
    papers = se.search(query)
    totalnum = len(papers)
    # 返回json
    response = {"totalNum": totalnum}
    response["resultData"] = papers
    return JsonResponse(response, safe=False)


def downloadView(request):
    # 获取pdf的id
    id = int(request.GET.get('id'))
    # res = {
    #     "pdfPath": ".../searcher/data/PDFs/xx.pdf",
    #     "videoPath": ".../searcher/data/videos/xx.*",
    # }
    # 暂时使用假数据，对接后使用下边一句
    # return HttpResponse(res["pdfPath"])

    with open(se.search_by_id(id)["pdfPath"], 'rb') as pdfExtract:
        response = HttpResponse(pdfExtract.read(), content_type='application/pdf')

    return response


def ajax_suggest(request):
    query = request.GET.get('query')
    # auto-complete
    # 暂时使用假数据, 对接后使用后一句
    # result = ["smart", "smart guys", "smart car", "smart and clever"]
    result = se.auto_complete(query)
    # 先定义出返回数据的格式
    res = {"status": None, "resultCount": None, "resultData": None}
    # 执行结果，OK表示成功，FALL表示失败
    if len(result) == 0:
        res["status"] = "FALL"
        res['resultCount'] = -1
    else:
        res["status"] = "OK"
        res['resultCount'] = len(result)
        res['resultData'] = result
    # 返回
    return JsonResponse(res)

# def downloadVideo(url, id):
#     res = requests.get(url, stream=True)
#     with open(str(id) + '.mp4', 'wb') as f:
#         for chunk in res.iter_content(chunk_size=10240):
#             f.write(chunk)

def pyMuPDF_fitz(pdfPath, imagePath):
    # print("imagePath=" + imagePath)
    print(pdfPath)
    print(imagePath)
    pdfDoc = fitz.open(pdfPath)
    if not pdfDoc:
        return
    # for pg in range(pdfDoc.pageCount):
    page = pdfDoc[0]
    rotate = int(0)
    # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
    # 此处若是不做设置，默认图片大小为：792X612, dpi=96
    zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
    zoom_y = 1.33333333
    mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    pix = page.getPixmap(matrix=mat, alpha=False)

    pix.writePNG(imagePath)  # 将图片写入指定的文件夹内