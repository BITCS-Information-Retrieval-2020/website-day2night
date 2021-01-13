
import redis
import json
import re
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .fake import get_detail, get_title, searchpapers


main_rds = redis.StrictRedis(host='localhost', port=6379, db=0, password='')


def detail(request):
    id = request.GET.get('id')
    main_rds.zincrby('hot', 1, id)
    data = get_detail(id)
    return HttpResponse(data)


def hot(request):
    num = int(request.GET.get('num'))
    if not num:
        num = 5
    if num < 0:
        return HttpResponse('Error! num can not < 1')
    hot_list = main_rds.zrevrange('hot', 0, num - 1, withscores=False)
    data = []
    for id in hot_list:
        data.append(get_title(id.decode()))
    data = json.dumps(data)
    return HttpResponse(data)


def results(request):
    # from ScienceSearcher.SearchEngine import SearchEngine

    # initialization
    # se = SearchEngine(download_server_ip='xxx.xxx.xxx.xxx',
    #                   download_server_port=5000,
    #                   download_client_ip='xxx.xxx.xxx.xxx',
    #         s          download_client_port=9001,
    #                   es_ip='xxx.xxx.xxx.xxx',
    #                   es_port=9200,
    #                   index_name='xxx',
    #                   video_index_name='xxx')

    # GET type and query
    type1 = int(request.GET.get('type'))
    q = request.GET.get('query')
    # generate dict
    query = {'top_number': 300}
    if int(type1) == 1:
        # 后端测试使用q
        q = {
            "title": "GNN",
            "author": "Hinton",
            "abstract": "",
            "content": "this paper proposed",
            "operator": ["OR", "AND", "", "NOT"],
        }
        operator = q["operator"]
        q.pop("operator")
        query["type"] = int(type1)
        query["query_text"] = q
        query["operator"] = operator
    else:
        query["type"] = int(type1)
        query["query_text"] = q

    # 测试使用
    papers = searchpapers(query)
    # 正式使用
    # papers = se.search(query)
    paginator = Paginator(papers, 10)
    page = request.GET.get('page')
    response = [paginator.num_pages]
    try:
        contacts = paginator.page(page)
        for contact in contacts:
            response.append(contact)
        # response['list'] = json.loads(serializers.serialize("json", contacts))
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        contacts = paginator.page(1)
        for contact in contacts:
            response.append(contact)
        # response['list'] = json.loads(serializers.serialize("json", contacts))
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        contacts = paginator.page(paginator.num_pages)
        for contact in contacts:
            response.append(contact)
        # response['list'] = json.loads(serializers.serialize("json", contacts))
    # return HttpResponse(json.dump(response, cls=DjangoJSONEncoder), content_type='application/json')
    return JsonResponse(response, safe=False)


def downloadView(request):
    # 获取pdf的id
    id = int(request.GET.get('_id'))
    res = {
        "pdfPath": ".../searcher/data/PDFs/xx.pdf",
        "videoPath": ".../searcher/data/videos/xx.*",
    }
    # 暂时使用假数据，对接后使用下边一句
    return HttpResponse(res["pdfPath"])
    # return HttpResponse(se.search_by_id(id)["pdfPath"])


def ajax_suggest(request):
    query = request.GET.get('query')
    # auto-complete
    # 暂时使用假数据, 对接后使用后一句
    result = ["smart", "smart guys", "smart car", "smart and clever"]
    # result = se.auto_complete(query)
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
