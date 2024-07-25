from django.shortcuts import render
from web.models import Category, Course


def index(request):
    # category = []

    category = Category.objects.all()
    course = Course.objects.all()[:4]

    context = {
        "categories": category,
        "courses" : course
    }

    return render(request, "index.html", context=context)

    


def singlepage(request):

    course = Course.objects.all()[:1]
    context = {
        "courses" : course
    }

    return render(request, "singlepage.html",context=context)


def courses(request):

    course = Course.objects.all()
    context = {
        "courses" : course
    }

    return render(request,"courses.html", context=context)
