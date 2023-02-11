from django.views import generic
from .models import Post
from django.contrib import messages
from django.urls import reverse_lazy


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = '__all__' 
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('my_list_view')
