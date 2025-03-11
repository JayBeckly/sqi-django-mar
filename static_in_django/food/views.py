from django.shortcuts import render

from . import views

# Create your views here.


def menu(request):
    return render(request, 'food/menu.html')
