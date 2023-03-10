from django.views import generic
from .models import Post
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('my_list_view')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin,generic.UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('my_list_view')

    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin,generic.DeleteView):
    model = Post
    success_url = reverse_lazy('my_list_view')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

