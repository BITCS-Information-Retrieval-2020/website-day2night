import json
import re

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Post, Category, Tag
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core import serializers
from bpmappers.djangomodel import ModelMapper
from bpmappers import RawField

class SubjectMapper(ModelMapper):
    # author = RawField('author')
    class Meta:
        model = Post
        exclude = ('author')


def index(request):
    post_list = Post.objects.all().order_by('-created_time')

    return render(request, 'blog/index.html', context={'post_list':post_list})

# def show_paperlist(request, page):
# def show_paperlist(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     paginator = Paginator(post_list, 10)
#     page = request.GET.get('page')
#     response = {}
#     try:
#         contacts = paginator.page(page)
#         response['list'] = json.loads(serializers.serialize("json", contacts))
#     except PageNotAnInteger:
#         # 如果用户请求的页码号不是整数，显示第一页
#         contacts = paginator.page(1)
#         response['list'] = json.loads(serializers.serialize("json", contacts))
#     except EmptyPage:
#         # 如果用户请求的页码号超过了最大页码号，显示最后一页
#         contacts = paginator.page(paginator.num_pages)
#         response['list'] = json.loads(serializers.serialize("json", contacts))
#
#     return JsonResponse(response)

def show_paperlist(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    response = []
    try:
        contacts = paginator.page(page)
        for contact in contacts:
            response.append(SubjectMapper(contact).as_dict())
        # response['list'] = json.loads(serializers.serialize("json", contacts))
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        contacts = paginator.page(1)
        for contact in contacts:
            response.append(SubjectMapper(contact).as_dict())
        # response['list'] = json.loads(serializers.serialize("json", contacts))
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        contacts = paginator.page(paginator.num_pages)
        for contact in contacts:
            response.append(SubjectMapper(contact).as_dict())
        # response['list'] = json.loads(serializers.serialize("json", contacts))

    return JsonResponse(response, safe=False)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    post.increase_views()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    # post.toc = md.toc
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post':post})

def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=tag).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})