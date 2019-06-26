from django.urls import path
from django.contrib.auth import views as auth_views
from groups.views import CreateGroup,SingleGroup,ListGroups,JoinGroup,LeaveGroup
app_name='groups'
urlpatterns = [
    path('',ListGroups.as_view(),name='all'),
    path('new/',CreateGroup.as_view(),name='create'),
    path('posts/in/<slug:slug>/',SingleGroup.as_view(),name='single'),
    path('join/<slug:slug>/',JoinGroup.as_view(),name='join'),
    path('leave/<slug:slug>/',LeaveGroup.as_view(),name='leave'),
]
