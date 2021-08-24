from django.urls import path

import category.views as views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('create-category/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<slug>/', views.CategoryDetailView.as_view(), name='category_detail')
]
