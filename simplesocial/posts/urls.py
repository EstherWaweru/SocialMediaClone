from django.urls import path
from django.contrib.auth import views as auth_views
from posts.views import DeletePost,PostDetail,UserPosts,CreatePost,PostList
app_name='posts'
urlpatterns = [
    path('',PostList.as_view(),name='all'),
    path('new/',CreatePost.as_view(),name='create'),
    path('by/<slug:username>/',UserPosts.as_view(),name='for_user'),
    path('by/<str:username>/<int:pk>/',PostDetail.as_view(),name='single'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='delete'),


]
