from django.urls import path

import category.views as views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('create-category/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category-update/<slug>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<slug>/', views.CategoryDeleteView.as_view(), name='category_delete')
]
