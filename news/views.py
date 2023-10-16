from django.shortcuts import render
from django.views import generic
from news.models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news/main.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'news/detail.html'


def error_404_view(request, exception):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, 'errors/404.html')
