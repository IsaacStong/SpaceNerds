from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Group, GroupMember
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

# Create your views here.
 class CreateGroup(LoginRequiredMixin, generic.CreateView):
     fields = ('name', 'description')
     model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
