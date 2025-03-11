from django.shortcuts import render

# Create your views here.


def food(request):
    context = {
        "food": ["Rice", "Beans", "yam"] 
    }

    return render(request,"test_app/food.html", context)