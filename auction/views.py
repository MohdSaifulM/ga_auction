from django.http.response import HttpResponse, HttpResponseRedirect
from auction.models import Category, Item
from django.urls import reverse
from django.shortcuts import render
# reads of the form.py
from .forms import NewCategoryForm, NewItemForm

# Create your views here.
# ============ Categories ===============


def index(request):
    if request.method == "POST":  # django
        form_data = NewCategoryForm(request.POST)  # django
        if form_data.is_valid():  # django
            name = form_data.cleaned_data['name']  # django
            # new Category(request.body)
            category = Category(name=name)
            # django
            category.save()  # django
        else:
            return HttpResponseRedirect(reverse("index"))  # django

    # Category.find() []
    categories = Category.objects.all()  # django
    form = NewCategoryForm()
    # django
    return render(request, 'auction/index.html', {"categories": categories, "form": form})


def show_category(request, id):
    cat = Category.objects.get(pk=id)
    # localhost:8000/show/id?del=true
    if request.GET.get("del") == "true":
        cat.delete()  # deletes on cat
        return HttpResponseRedirect(reverse("index"))

    elif request.method == "POST":
        form_data = NewCategoryForm(request.POST, instance=cat)  # django
        if form_data.is_valid():  # django
            form_data.save()  # save data to db
            # particular page
            # redirect to the page with the id
            #  the "," at the end is part of the code
            return HttpResponseRedirect(reverse("show_category", args=(cat.id,)))

    form = NewCategoryForm(instance=cat)

    return render(request, 'auction/show.html', {"category": cat, "form": form})


# ============ Listing for Items ===============

def listing(request):

    if request.method == 'POST':
        form_data = NewCategoryForm(request.POST)  # django
        if form_data.is_valid():  # django
            name = form_data.cleaned_data['name']
            price = form_data.cleaned_data['price']
            description = form_data.cleaned_data['description']
            img_url = form_data.cleaned_data['img_url']

            item = Item(name=name, price=price,
                        description=description, img_url=img_url)
            # django
            item.save()  # django
        else:
            return HttpResponseRedirect(reverse("listing"))  #

    items = Item.objects.all()
    return render(request, "auction/items.html", {"items": items, "form": NewItemForm()})


def list_item(request, id):
    item = Item.objects.get(pk=id)

    if request.GET.get("del") == "true":
        item.delete()  # deletes on cat
        return HttpResponseRedirect(reverse("listing"))

    elif request.method == "POST":
        form_data = NewItemForm(request.POST, instance=item)  # django
        if form_data.is_valid():  # django
            form_data.save()  # save data to db
            # particular page
            # redirect to the page with the id
            #  the "," at the end is part of the code
            return HttpResponseRedirect(reverse("show_category", args=(item.id,)))

    return render(request, "auction/item.html", {"item": item, "form": NewItemForm(instance=item)})
