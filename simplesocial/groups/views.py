from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,RedirectView
from groups.models import Group,GroupMember
from django.shortcuts import get_object_or_404
from django.contrib import messages
from . import models

# Create your views here.
class CreateGroup(LoginRequiredMixin,CreateView):
    fields=['name','description']
    model=Group
class SingleGroup(DetailView):
    model=Group
class ListGroups(ListView):
    model=Group
class JoinGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self,request,*args,**kwargs):
        group=get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,('Already a member'))
        else:
            messages.success(self.request,'You are now a member')
        return super().get(request,*args,**kwargs)
class LeaveGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self,request,*args,**kwargs):
        try:
            membership = models.GroupMember.objects.filter(user = self.request.user,group__slug = self.kwargs.get('slug')).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry not a member for the group')
        else:
            membership.delete()
            messages.success(self.request,'You have left this group')
        return super().get(request,*args,**kwargs)
