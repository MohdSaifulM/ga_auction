from auction.models import Category
from django.shortcuts import render
from django import forms


#  form information
class NewCategoryForm(forms.Form):
    name = forms.CharField(min_length=4, max_length=60)


# Create your views here.
def index(request):
    categories = Category.objects.all()

    return render(request, 'auction/index.html', {"categories": categories, "form": NewCategoryForm()})


def show(request):
    return render(request, 'auction/show.html')
