from django.shortcuts import render
from .models import MoviesData
from django.views.generic.list import ListView
from django.core.paginator import Paginator

# Create your views here.

"""
class MovieList(ListView):
    model = MoviesData
    template_name = 'movies/movies-list.html'
    context_object_name = 'movies_list'
"""
def movie_list(request):
    movie_list = MoviesData.objects.all()

    movie_search = request.GET.get('movie_search')

    if movie_search != '' and movie_search is not None:
        movie_list = movie_list.filter(name__icontains = movie_search)

    pagination = Paginator(movie_list, 3)
    page = request.GET.get('page')
    movie_list = pagination.get_page(page)

    return render(request, 'movies/movies-list.html',  { 'movie_list' : movie_list})