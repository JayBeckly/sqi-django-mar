from django.shortcuts import render, HttpResponse

# Create your views here.


def home(requests):
    return HttpResponse("Welcome To The Homepage")

# def contact(requests):