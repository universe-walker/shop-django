from django.shortcuts import render, HttpResponse


def base_view(request):
    return HttpResponse('Hello!')
