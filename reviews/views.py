from django.shortcuts import render, redirect
from django.contrib import messages

from reviews.forms import MovieForm
from reviews.models import Review, Product


def add_review(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.product = Product.object.get(id=1)
            movie_form.save()
            # messages.success(request, ('Your movie was successfully added!'))
        else:
            messages.error(request, 'Error in saving form.')

        return redirect("users-home")
    movie_form = MovieForm()
    movies = Review.objects.all()
    return render(request=request, template_name="review.html", context={'form': movie_form, 'movies': movies})


def product_list(request):
    products = Product.objects.all()
    return render(request=request, template_name="product_list.html", context={'products': products})

def contactus(request):
    return render(request=request, template_name="contactus.html")

def services(request):
    return render(request=request, template_name="services.html")

def aboutus(request):
    return render(request=request, template_name="aboutus.html")