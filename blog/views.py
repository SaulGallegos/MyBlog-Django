from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm, EditPostForm

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
     form_class = PostForm
     template_name = 'add_post.html'

##############
## Add Post ##
##############
class UpdatePostView(UpdateView):
     model = Post
     form_class = EditPostForm
     template_name = 'update_post.html'
