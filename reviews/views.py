from django.shortcuts import render, redirect
from django.contrib import messages

from reviews.forms import MovieForm
from reviews.models import Review, Product


def add_review(request, id):
    if request.method == "POST":
        review_form = MovieForm(request.POST, request.FILES)
        if review_form.is_valid():
            review_form = review_form.save(commit=False)
            pid = Product.objects.get(id=id)
            review_form.product = pid

            review_form.user_id = request.user.id
            review_form.save()
            # messages.success(request, ('Your movie was successfully added!'))
        else:
            messages.error(request, 'Error in saving form.')

        return redirect("product_list")
    review_form = MovieForm()
    product = Product.objects.get(id=id)
    return render(request=request, template_name="review.html", context={'form': review_form, 'product': product, 'product_id': id})


def my_review(request):
    review = Review.objects.filter(user=request.user)
    return render(request=request, template_name="myreview.html",
                  context={ 'review': review})

def product_list(request):
    products = Product.objects.all()
    return render(request=request, template_name="product_list.html", context={'products': products})

def contactus(request):
    return render(request=request, template_name="contactus.html")

def services(request):
    return render(request=request, template_name="services.html")

def aboutus(request):
    return render(request=request, template_name="aboutus.html")