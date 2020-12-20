from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import Post

# Create your views here.

# without pagination
# def post_list(request):
#     posts = Post.published.all()
#     context = { 'posts': posts}
#     return render(request, 'post/list.html', context)

#with django build-in pagination
# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 2) # 2 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#     # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#     # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     context = {'page': page,'posts': posts}
#     return render(request, 'post/list.html', context)

#class-based view
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    
    context = {'post': post}
    return render(request, 'post/detail.html', context)