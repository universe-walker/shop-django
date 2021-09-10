from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory

from .models import Category, Product, Characteristic


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'img', 'parent']


class CategoryUpdateForm(CategoryCreateForm):
    ...


class ProductCreateForm(ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Картинка')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'available_count', 'category']


class CharacteristicCreateForm(ModelForm):
    class Meta:
        model = Characteristic
        fields = ['name', 'value']


CharacteristicCreateFormSet = modelformset_factory(Characteristic,
                                                   form=CharacteristicCreateForm,
                                                   extra=20)
