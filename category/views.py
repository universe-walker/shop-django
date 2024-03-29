from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.views import View

from .models import Category, Product, ProductImage, Characteristic
from .forms import (
    CategoryCreateForm,
    CategoryUpdateForm,
    ProductCreateForm,
    CharacteristicCreateFormSet,
)
from .filters import ProductFilter


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/category_create.html'
    form_class = CategoryCreateForm


class CategoryProductListView(ListView):
    model = Product
    template_name = 'category/category_detail.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_characteristics(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return Characteristic.objects.filter(product__category=category).all()

    def get_filter(self, queryset=None):
        products = Product.objects.filter(category=Category.objects.get(slug=self.kwargs['slug'])).all()
        ProductFilter.declared_filters['characteristic'].queryset = queryset
        return ProductFilter(self.request.GET, queryset=products)

    def get_queryset(self, **kwargs):
        return self.get_filter(self.get_characteristics()).qs

    def get_context_data(self, **kwargs):
        context = super(CategoryProductListView, self).get_context_data()
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['filter'] = self.get_filter(queryset=self.get_characteristics())
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


class SearchAdvice(View):
    def get(self, request):
        q = request.GET.get('q')
        if q:
            return JsonResponse({'products': list(Product.objects.filter(name__icontains=q).values('name')[:5])})
        return JsonResponse({})


class CharacteristicCreateView(CreateView):
    model = Characteristic
    form_class = CharacteristicCreateFormSet
    template_name = 'category/characteristic_create.html'

    def get_form(self, form_class=None):
        product = Product.objects.get(slug=self.kwargs['slug'])
        formset = CharacteristicCreateFormSet(queryset=Characteristic.objects.filter(product=product))
        return formset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        context['product'] = Product.objects.get(slug=context['slug'])
        context['characteristics'] = context['product'].characteristics.all()
        return context

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(slug=kwargs['slug'])
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            instances = bound_form.save(commit=False)
            for i in instances:
                i.product = product
                i.save()
            return HttpResponseRedirect(product.get_absolute_url())
        return render(request, template_name=self.template_name, context={'form': bound_form, 'slug': kwargs['slug']})


class CheckEmailView(View):
    def get(self, request, *args, **kwargs):
        email = request.GET['email'][0]
        if User.objects.filter(email=email).exists():
            return HttpResponse('EXIST')
        else:
            return HttpResponse('OK')
