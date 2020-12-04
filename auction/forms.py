from auction.models import Category, Item
from django import forms

#  form information


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description', 'sold']
        # adding class to form field
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    # name = forms.CharField(min_length=4, max_length=60,
    #                        label="New Category", widget=forms.TextInput(attrs={'class': "form-control"}))
