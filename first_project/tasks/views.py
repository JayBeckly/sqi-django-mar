from django.shortcuts import render, HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse("Welcome to homepage")


def alltask(request):
    return HttpResponse("View all tasks here")