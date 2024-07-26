from django.urls import path
from web.views import index, singlepage, courses
from . import views


app_name = 'web'

urlpatterns = [
    path('',index,name="index"),
    path('singlepage/<int:course_id>/',singlepage,name="singlepage"),
    path('courses/',courses,name="courses"),
    path('category/<int:category_id>/',views.category_courses,name="category_courses")
]