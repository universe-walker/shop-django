from django.forms import ModelForm
from django import forms

from .models import Category, Product, ProductImage


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'img', 'parent']


class CategoryUpdateForm(CategoryCreateForm):
    ...


class ProductCreateForm(ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='картинка')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'available_count', 'category']
