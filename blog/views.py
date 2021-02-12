from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

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


##############
## Add Post ##
##############
class AddPostView(CreateView):
     model = Post
     template_name = 'add_post.html'
     fields = '__all__'
     