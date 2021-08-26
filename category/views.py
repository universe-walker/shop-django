from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Category, Product, ProductImage
from .forms import CategoryCreateForm, CategoryUpdateForm, ProductCreateForm


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'category/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'category/product_create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        print(images, 'images')
        if form.is_valid():
            instance = form.save()
            ProductImage.objects.bulk_create([ProductImage(path=i, product=instance) for i in images])
            return HttpResponseRedirect(instance.get_absolute_url())
        return render(request, template_name=self.template_name, context={'form': form})
