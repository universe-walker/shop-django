from django.urls import path

import category.views as views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('create-category/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<slug>/', views.CategoryProductListView.as_view(), name='category_detail'),
    path('category-update/<slug>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<slug>/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('product/<slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('create-product/', views.ProductCreateView.as_view(), name='product_create'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('search-advice/', views.SearchAdvice.as_view(), name='search_advice')
]
