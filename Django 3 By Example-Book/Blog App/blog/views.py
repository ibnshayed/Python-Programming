from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Count

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail

from .models import Post, Comment
from taggit.models import Tag


# Create your views here.

# Class-based view
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts' # object_list generates by default
    paginate_by = 2
    template_name = 'post/list.html'

# Get a single Post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            # .save() only comes with ModelForm not Form
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                        .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                 .order_by('-same_tags','-publish')[:4]
    context = {
                'post': post,
                'comments': comments,
                'new_comment': new_comment,
                'comment_form': comment_form,
                'similar_posts': similar_posts,
              }

    return render(request, 'post/detail.html', context)



# Post Share by Email with google SMTP server
def post_share(request, post_id):
    # Retrived post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():

           cd = form.cleaned_data # is return a dictionary based form value
           post_url = request.build_absolute_uri(post.get_absolute_url())
           subject = f"{cd['name']} recommends you read {post.title}"
           message = f"Read {post.title} at {post_url}\n\n" \
                     f"{cd['name']}\'s comments: {cd['comments']}"
           send_mail(subject, message, 'your_account@mail.com',[cd['to']])
           sent = True
    else:
        form = EmailPostForm()
    context = {'post': post, 'form': form, 'sent': sent}
    return render(request, 'post/share.html', context)


# without pagination
# def post_list(request):
#     posts = Post.published.all()
#     context = { 'posts': posts}
#     return render(request, 'post/list.html', context)

#with django build-in pagination
def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 2) # 2 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    context = {'page': page,'posts': posts, 'tag': tag}
    return render(request, 'post/list.html', context)


# Creating search form
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # results = Post.published.annotate(search=SearchVector('title', 'body'),).filter(search=query)

            # search_vector = SearchVector('title', 'body')

            search_vector = SearchVector('title', weight='A') + \
                            SearchVector('body', weight='B')

            search_query = SearchQuery(query)
            # results = Post.published.annotate(
            #             search=search_vector,
            #             rank=SearchRank(search_vector, search_query)
            #             ).filter(search=search_query).order_by('-rank')

            # With weight
            # results = Post.published.annotate(
            #             search=search_vector,
            #             rank=SearchRank(search_vector, search_query)
            #             ).filter(rank__gte=0.3).order_by('-rank')

            # With trigram similarity
            results = Post.published.annotate(
                        similarity=TrigramSimilarity('title', query),
                        ).filter(similarity__gt=0.1).order_by('-similarity')
    context = {
                'form': form,
                'query': query,
                'results': results
              }
    return render(request,'post/search.html',context)