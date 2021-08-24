from django.urls import path

import category.views as views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
]
