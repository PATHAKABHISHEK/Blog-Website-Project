from django.shortcuts import render

# Create your views here.

def show_blogs(request):
    return render(request, 'show_blogs.html')