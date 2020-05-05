from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required


def blog_home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'myblog/post_list.html', context)
class PostListView(ListView):
    model = Post
    template_name = 'myblog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = '/blog/myblog_home/'

@login_required
def contact(request):

    return render(request,'myblog/contact.html',{'title':'contact'})
@login_required
def sent(request):

    return render(request,'myblog/sent.html',{'title':'email_sent'})


def home(request):

    return render(request,'myblog/home.html',{'title':'home'})


def about(request):
    return render(request,'myblog/about.html',{'title':'about'})


def services(request):
    return render(request,'myblog/services.html',{'title':'services'})