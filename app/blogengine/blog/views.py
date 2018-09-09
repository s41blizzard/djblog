from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from django.views.generic import View


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


# def post_details(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_details.html', context={'post': post})


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_details.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all
    return render(request, 'blog/tags_list.html', context={'tags': tags})


# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': tag})
