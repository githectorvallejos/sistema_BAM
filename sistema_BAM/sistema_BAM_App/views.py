from django.shortcuts import render
from .models import bam_usuario

# Creacion de vistas

def home(request):
    bam = bam_usuario.objects.all()
    return render(request, "home.html", {"bams": bam})
