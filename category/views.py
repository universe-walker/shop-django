from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views import View

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


class CategoryProductListView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryProductListView, self).get_context_data()
        context['products'] = Product.objects.filter(category=self.object).all()
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context


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


class SearchListView(ListView):
    template_name = 'category/search_list.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        if q := self.request.GET.get('q'):
            return Product.objects.filter(name__icontains=q)
        return None
