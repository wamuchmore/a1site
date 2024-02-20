from django.shortcuts import render

def home1(request):
    return render(request, "studio/home1.html", {})


