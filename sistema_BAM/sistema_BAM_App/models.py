from django.db import models

# Create your models here.
class bam_usuario(models.Model):
    id= models.CharField(primary_key=True, max_length=6)
    marca_modelo = models.CharField(max_length=20)
    Proveedor = models.CharField(max_length=20)
    linea=models.CharField(max_length=10)
    imei=models.CharField(max_length=15)
    sn=models.CharField(max_length=20)
    sim=models.CharField(max_length=20)
    apellido_nombre=models.CharField(max_length=50)
    dni=models.CharField(max_length=9)
    fecha=models.DateField()
