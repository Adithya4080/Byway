from django.shortcuts import render
from web.models import Category


def index(request):
    # category = []

    category = Category.objects.all()

    context = {
        "categories": category
    }

    return render(request, "index.html", context=context)

    


def singlepage(request):
    return render(request, "singlepage.html")
