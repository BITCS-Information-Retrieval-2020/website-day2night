import json
import re

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post, Category, Tag
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core import serializers
from bpmappers.djangomodel import ModelMapper
from bpmappers import RawField
from django.core.serializers.json import DjangoJSONEncoder
from .fakedata import Papers

def index(request):
    # post_list = Post.objects.all().order_by('-created_time')

    return render(request, 'blog/index.html')

def results(request):
    type1 = int(request.GET.get('type'))
    req = request.GET.get('query')
    # print(req, type(req))
    # print(type1, type(type1))
    papers = Papers().searchpapers(type=type1, req=req, topnum=100)
    paginator = Paginator(papers, 10)
    page = request.GET.get('page')
    # print(page, type(page))
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

# global REQ
# # @csrf_exempt
# def showfirstpaperlist(request):
#     papers = []
#     if request.method == 'GET':
#         REQ = request.GET.get('q')
#         # REQ = json.loads(request.body) #取得前端数据
#         papers = Papers().searchpapers(REQ)
#         paginator = Paginator(papers, 10)
#         page = request.GET.get('page')
#         response = []
#         contacts = paginator.page(1)
#         for contact in contacts:
#             response.append(contact)
#         # print(0)
#         return JsonResponse(response, safe=False)
#     else:
#         return JsonResponse({'error': 'error'}, safe=False)




# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # post.body = markdown.markdown(post.body,
#     #                               extensions=[
#     #                                   'markdown.extensions.extra',
#     #                                   'markdown.extensions.codehilite',
#     #                                   'markdown.extensions.toc',
#     #                               ])
#     post.increase_views()
#     md = markdown.Markdown(extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         TocExtension(slugify=slugify),
#     ])
#     post.body = md.convert(post.body)
#     # post.toc = md.toc
#     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#     post.toc = m.group(1) if m is not None else ''
#
#     return JsonResponse(post, safe=False)




