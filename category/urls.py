from django.urls import path

import category.views as views

urlpatterns = [
    path('', views.base_view, 'base_view'),
]
