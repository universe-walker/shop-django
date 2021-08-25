from django.forms import ModelForm

from .models import Category, Product


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'img', 'parent']


class CategoryUpdateForm(CategoryCreateForm):
    ...


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'available_count', 'category']
