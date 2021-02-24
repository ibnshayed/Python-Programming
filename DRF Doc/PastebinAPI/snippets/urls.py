from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import views

# this is needed for start_project include namespace
app_name = 'snippets'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })


# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('list/', snippet_list, name='snippet-list'),
#     path('<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])


# urlpatterns = [

#     # path('users/', views.UserList.as_view()),
#     # path('users/<int:pk>/', views.UserDetail.as_view()),

#     path('users/',views.UserList.as_view(),name='user-list'),
#     path('users/<int:pk>/',views.UserDetail.as_view(),name='user-detail'),

#     # path('', views.index, name='index'),
#     # path('', views.snippet_list),
#     # path('<int:pk>/', views.snippet_detail),

#     # Classed based view
#     # path('list', views.SnippetList.as_view()),
#     # path('<int:pk>/', views.SnippetDetail.as_view()),

#     # path('', views.api_root),
#     # path('<int:pk>/highlight/', views.SnippetHighlight.as_view()),

#     path('', views.api_root),
#     path('list/',views.SnippetList.as_view(),name='snippet-list'),
#     path('<int:pk>/',views.SnippetDetail.as_view(),name='snippet-detail'),
#     path('<int:pk>/highlight/',views.SnippetHighlight.as_view(),name='snippet-highlight'),
    

# ]

# urlpatterns = format_suffix_patterns(urlpatterns)