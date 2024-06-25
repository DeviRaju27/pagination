from django.shortcuts import render
from .models import MoviesData
from django.views.generic.list import ListView

# Create your views here.

class MovieList(ListView):
    model = MoviesData
    template_name = 'movies/movies-list.html'
    context_object_name = 'movies_list'