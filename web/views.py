from django.shortcuts import render
from django.shortcuts import get_object_or_404
from web.models import Category, Course


def index(request):

    category = Category.objects.all()
    course = Course.objects.all()[:4]

    context = {
        "categories": category,
        "courses" : course
    }

    return render(request, "index.html", context=context)

    


def singlepage(request,course_id):

    course = get_object_or_404(Course, id=course_id)
    original_price = course.original_price
    discount_percentage = course.discount_price
    new_price = original_price - (original_price * (discount_percentage / 100))

    context = {
        "courses" : course,
        'new_price': new_price
    }

    return render(request, "singlepage.html",context=context)


def courses(request):

    course_list = Course.objects.all()
    for course in course_list:
        original_price = course.original_price
        discount_percentage = course.discount_price
        course.new_price = original_price - (original_price * (discount_percentage / 100))
    
    context = {
        "courses" : course_list
    }

    return render(request,"courses.html", context=context)
