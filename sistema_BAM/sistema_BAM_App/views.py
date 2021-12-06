from django.shortcuts import render, HttpResponse

# Creacion de vistas

def home(request):
    return render(request, "home.html")
