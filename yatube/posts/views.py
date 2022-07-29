from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUM_OF_OBJECTS = 10


def index(request):
    """ View-функция основной страницы"""
    posts = Post.objects.order_by('-pub_date')[:NUM_OF_OBJECTS]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """View-функция для страницы сообщества:"""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUM_OF_OBJECTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
