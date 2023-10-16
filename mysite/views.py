from django.shortcuts import render
from django.views import generic


def home(request):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, 'index.html')
