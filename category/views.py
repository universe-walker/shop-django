from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Category
from .forms import CategoryCreateForm, CategoryUpdateForm


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/category_create.html'
    form_class = CategoryCreateForm


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category/category_update.html'
    context_object_name = 'category'
    form_class = CategoryUpdateForm


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')

