from django.db import models

# Create your models here.
class productos(models.Model):

    nombre = models.CharField(max_length=20)
    seccion = models.CharField(max_length=20)
    precio = models.FloatField()
    imagen = models.CharField(max_length=100)
    stock = models.IntegerField()
    vendedor = models.CharField(max_length=20)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        db_table='productos'   #nombre de la base de datos en mysql
        ordering=['id']


class ordenes(models.Model):
    comprador = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(productos, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    code_hash = models.CharField(max_length=250, default='none')

    class Meta:
        verbose_name='ordenes'
        verbose_name_plural='ordenes'
        db_table='ordenes'
        ordering=['id']
