from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView, DetailView

from .models import Category
from .forms import CategoryCreateForm


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/category_create.html'
    form_class = CategoryCreateForm


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'

