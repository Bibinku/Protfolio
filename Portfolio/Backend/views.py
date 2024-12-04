from django.shortcuts import render,redirect


# Create your views here.

def indexpage(req):
    return render(req,"index.html")
