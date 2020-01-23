from django.shortcuts import render

from .models import Post, Tag
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'napominalka/index.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'napominalka/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'napominalka/tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'napominalka/tag_detail.html', context={'tag': tag})
