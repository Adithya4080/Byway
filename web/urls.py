from django.urls import path
from web.views import index, singlepage


app_name = 'web'

urlpatterns = [
    path('',index,name="index"),
    path('singlepage/',singlepage,name="singlepage")
]