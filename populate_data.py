import os
import django
import random
from faker import Faker

#confi django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitealmacen.settings')
django.setup()

from MyApps.clientes.models import Cliente
from MyApps.productos.models import TipoProducto, Producto
from MyApps.ventas.models import Venta, VentaProducto
from django.contrib.auth.models import User

fake = Faker()

def create_clientes(n=50):
    for _ in range(n):
        Cliente.objects.create(
            nombre=fake.name(),
            direccion=fake.address(),
            telefono=fake.phone_number()[:12], #limitar a 12 caracteres
            correo=fake.unique.email(),
            password=fake.password(length=10), #generar una contraseña de 10 caracteres


        )

def create_tipo_productos(n=10):
    for _ in range(n):
        TipoProducto.objects.create(
            nombre=fake.word()
        )

def create_productos(n=20):
    tipo_productos = list(TipoProducto.objects.all())
    for _ in range(n):
        Producto.objects.create(
            nombre=fake.word(),
            marca=fake.company(),
            precio=round(random.uniform(10.0, 100.0), 2),
            stockmin=random.randint(1, 10),
            cantidad=random.randint(10, 100),
            tipoproducto=random.choice(tipo_productos),
        )

def create_ventas(n=100):
    clientes = list(Cliente.objects.all())
    usuarios = list(User.objects.all())
    for _ in range(n):
        Venta.objects.create(
            fecha = fake.date(),
            descuento = round(random.uniform(0.0, 10.0), 2),
            total = round(random.uniform(100.0, 1000.0), 2),
            subtotal = round(random.uniform(90.0, 990.0), 2),
            usuario = random.choice(usuarios),
            #producto = 
            #created = 
            #updated =
            cliente = random.choice(clientes)
        )

def create_venta_productos(n=200):
    ventas = list(Venta.objects.all())
    productos = list(Producto.objects.all())
    for _ in range(n):
        venta = random.choice(ventas)
        producto =random.choice(productos)
        cantidad = random.randint(1, 10)
        VentaProducto.objects.create(
            producto=producto,
            venta=venta,
            fechaVenta=fake.date_time(),
            precio=producto.precio,
            cantidad=cantidad,
            total=round(producto.precio * cantidad, 2)
        )

if __name__ == '__main__':
    print("Creando datos falsos...")
    create_clientes()
    create_tipo_productos()
    create_productos()
    create_ventas()
    create_venta_productos()
    print("Datos falsos creados con exito...")

#python3 populate_data.py 