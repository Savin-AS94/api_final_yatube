from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)

api_router = DefaultRouter()
api_router.register('posts', PostViewSet, basename='posts')
api_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
api_router.register(r'groups', GroupViewSet)
api_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(api_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
