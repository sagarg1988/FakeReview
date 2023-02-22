from django.shortcuts import render, redirect
from django.contrib import messages

from reviews.forms import MovieForm
from reviews.models import Review


def add_review(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.save()
            # messages.success(request, ('Your movie was successfully added!'))
        else:
            messages.error(request, 'Error in saving form.')

        return redirect("users-home")
    movie_form = MovieForm()
    movies = Review.objects.all()
    return render(request=request, template_name="review.html", context={'form': movie_form, 'movies': movies})