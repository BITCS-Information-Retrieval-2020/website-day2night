from django.http import HttpResponse
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
from .fake import get_detail,get_title,searchpapers


main_rds = redis.StrictRedis(host='localhost',port=6379,db=0,password='')


def detail(request):
    id = request.GET.get('id')
    main_rds.zincrby('hot',1,id)
    data=get_detail(id)
    return HttpResponse(data)

def hot(request):
    num = int(request.GET.get('num'))
    if not num:
        num=5
    if num<0:
        return HttpResponse('Error! num can not < 1')
    hot_list=main_rds.zrevrange('hot', 0, num-1, withscores=False)
    data=[]
    for id in hot_list:
        data.append(get_title(id.decode()))
    data=json.dumps(data)
    return HttpResponse(data)

def results(request):
    type1 = int(request.GET.get('type'))
    req = request.GET.get('query')
    papers = searchpapers(type=type1, req=req, topnum=100)
    paginator = Paginator(papers, 10)
    page = request.GET.get('page')
    response = []
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
