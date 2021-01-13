import json
import re

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .fakedata import Papers


def index(request):
    # post_list = Post.objects.all().order_by('-created_time')

    return render(request, 'blog/index.html')


def results(request):
    type1 = int(request.GET.get('type'))
    req = request.GET.get('query')
    papers = Papers().searchpapers(type=type1, req=req, topnum=100)
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
