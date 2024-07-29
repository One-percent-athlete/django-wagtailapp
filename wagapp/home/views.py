from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post

def post_list(request):
    posts = Post.objects.all()

    post_per_page = 3
    paginator = Paginator(posts, post_per_page)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {'posts': posts, 'page_object': page_object}
    return render(request, 'home/index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug,)
    context = {"post": post,}
    return render(request, 'home/detail.html', context)

