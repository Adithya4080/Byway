from django.urls import path
from web.views import index, singlepage, courses


app_name = 'web'

urlpatterns = [
    path('',index,name="index"),
    path('singlepage/',singlepage,name="singlepage"),
    path('courses/',courses,name="courses")
]