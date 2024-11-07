from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el Nombre del Cliente")
    direccion = models.CharField(max_length=100, help_text="Ingrese la Direccion del Cliente")
    telefono = models.CharField(max_length=12, help_text="Ingrese el Telefono del Cliente")
    correo = models.EmailField(max_length=100, help_text="Ingrese el Correo del Cliente")
    password = models.CharField(max_length=100, help_text="Ingrese el Password del Cliente")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
