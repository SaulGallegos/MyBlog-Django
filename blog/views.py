from django.urls.base import reverse_lazy
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


###############
# Delete Post #
###############
class DeletePostView(DeleteView):
     model = Post
     template_name = 'delete_post.html'
     success_url = reverse_lazy('home')
