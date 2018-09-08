from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Tag


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def post_details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_details.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all
    return render(request, 'blog/tags_list.html', context={'tags': tags})