from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def singlepage(request):
    return render(request, "singlepage.html")
