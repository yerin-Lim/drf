from django.urls import path, include
from . import views
from .views import SnippetViewset, UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


#Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

#The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
"""
밑에 있는 것을 위에 것으로 refactoring
위에 있는 것이 더 유용한 추상화. 하지만 개별적으로 작성한 것보다
덜 명확. 나중에 고치기 힘듬
참고하여 사용!


snippet_list = SnippetViewSet.as_view({
    'get':'list',
    'post: 'create',
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes = [renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name = 'snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name = 'snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name = 'user-detail'),
])
"""