from django.shortcuts import render

def index(request):
    context = {} # Initialize an empty context for now
    return render(request, "home/index.html",context)