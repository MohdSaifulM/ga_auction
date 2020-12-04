from django.http.response import HttpResponse, HttpResponseRedirect
from auction.models import Category, Item
from django.urls import reverse
from django.shortcuts import render
from django import forms


#  form information
class NewCategoryForm(forms.Form):
    name = forms.CharField(min_length=4, max_length=60)


# Create your views here.
def index(request):
    if request.method == "POST":  # django
        form_data = NewCategoryForm(request.POST)  # django
        if form_data.is_valid():  # django
            name = form_data.cleaned_data['name']  # django
            # new Category(request.body)
            category = Category(name=name)  # django

            category.save()  # django
        else:
            return HttpResponseRedirect(reverse("index"))  # django

    # Category.find() []
    categories = Category.objects.all()  # django
    # django
    return render(request, 'auction/index.html', {"categories": categories, "form": NewCategoryForm()})


def show(request):
    return render(request, 'auction/show.html')


def listing(request):
    items = Item.objects.all()

    return render(request, "auction/items.html", {"items": items})


def list_item(request, id):
    item = Item.objects.get(pk=id)

    return render(request, "auction/item.html", {"item": item})
