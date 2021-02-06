from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView

##############
#### HOME ####
##############
class HomeView(ListView):
     model = Post
     template_name = 'home.html'


##############
### Detail ###
##############
class PostDetailView(DetailView):
     model = Post
     template_name = 'post_details.html'