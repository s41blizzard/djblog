from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixIn, ObjectDeleteMixIn
from .forms import TagForm, PostForm


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_details.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


class PostUpdate(ObjectUpdateMixIn, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'

class PostDelete(ObjectDeleteMixIn, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'


def tags_list(request):
    tags = Tag.objects.all
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixIn, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(ObjectDeleteMixIn, View):
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/tag_delete_form.html', context={'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
