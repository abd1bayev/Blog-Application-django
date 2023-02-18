from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404



def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    print(posts)

    return render(request, 'blog/post/list.html', context)


def post_detail(request, id):

    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)

    return render(request,
                  'blog/post/detail.html',
                  {'post': post})