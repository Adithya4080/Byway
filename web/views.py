from django.shortcuts import render
from django.shortcuts import get_object_or_404
from web.models import Category, Course


def index(request):

    categories = Category.objects.all()
    courses = Course.objects.all()[:4]

    for category in categories:
        category.total_courses = Course.objects.filter(category=category).count()

    for course in courses:
        original_price = course.original_price
        discount_percentage = course.discount_price
        course.new_price = original_price - (original_price * (discount_percentage / 100))

    context = {
        "categories": categories,
        "courses" : courses
    }

    return render(request, "index.html", context=context)

    
def category_courses(request, category_id):
    print(f"Received category_id: {category_id}") 
    category = get_object_or_404(Category, id=category_id)
    courses = Course.objects.filter(category=category)

    for course in courses:
        original_price = course.original_price
        discount_percentage = course.discount_price
        course.new_price = original_price - (original_price * (discount_percentage / 100))

    context = {
        "category": category,
        "courses": courses
    }

    return render(request, "categorys.html", context=context)


def singlepage(request,course_id):
    course = get_object_or_404(Course, id=course_id)
    original_price = course.original_price
    discount_percentage = course.discount_price
    new_price = original_price - (original_price * (discount_percentage / 100))
    category = course.category
    similar_courses = Course.objects.filter(category=category).exclude(id=course_id).distinct()[:4]

    for similar_course in similar_courses:
        original_price = similar_course.original_price
        discount_percentage = similar_course.discount_price
        similar_course.new_price = original_price - (original_price * (discount_percentage / 100))

    context = {
        "courses" : course,
        'new_price': new_price,
        'similar_courses': similar_courses
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

def categorys(request):
    return render(request, "categorys.html")