from django.db import models
from django.contrib.auth.models import User
from .choices import opciones

# Create your models here.

    
class Libro(models.Model):
    titulo_libro = models.CharField(max_length=200)
    descripcion_libro = models.TextField()
    portada = models.ImageField(upload_to='libros', null=True)
    ruta = models.CharField(max_length=300, null=True)
    updated_libro = models.DateTimeField(auto_now = True)
    created_libro = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.titulo_libro
    
class Autor(models.Model):
    nombre_autor = models.CharField(max_length=50)
    apellido_autor = models.CharField(max_length=50)
    biografia = models.TextField(null=True)
    updated_autor = models.DateTimeField(auto_now = True)
    created_autor = models.DateTimeField(auto_now_add = True)
    def nombre_completo(self):
        return "{}, {}".format(self.nombre_autor, self.apellido_autor)
    def __str__(self):
        return self.nombre_completo()

class Genero(models.Model):
    nombre_genero = models.CharField(max_length=100)
    updated_genero = models.DateTimeField(auto_now = True)
    created_genero = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.nombre_genero

class Valoracion(models.Model):
    comentario = models.TextField()
    puntos = models.CharField(max_length=1, choices=opciones, default=0)
    id_libroV = models.ForeignKey(Libro, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    updated_valoracion = models.DateTimeField(auto_now=True)
    created_valoracion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comentario

class Genero_libro(models.Model):
    id_libroG = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_generoL = models.ForeignKey(Genero, on_delete=models.CASCADE)
    updated_gl = models.DateTimeField(auto_now=True)
    created_gl = models.DateTimeField(auto_now_add=True)
    def genero_completo(self):
        return "{}, {}".format(self.id_libroG, self.id_generoL)
    def __str__(self):
        return self.genero_completo()

class Autor_libro(models.Model):
    id_libroA = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_autorL = models.ForeignKey(Autor, on_delete=models.CASCADE)
    updated_al = models.DateTimeField(auto_now=True)
    created_al = models.DateTimeField(auto_now_add=True)
    def detalle(self):
        return "{}, {}".format(self.id_autorL, self.id_libroA)
    def __str__(self):
        return self.detalle()

class Libro_usuario(models.Model):
    id_userL = models.ForeignKey(User, null= True, on_delete=models.SET_NULL)
    id_libroU = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_valoracionlu = models.ForeignKey(Valoracion, on_delete=models.CASCADE)
    updated_lu = models.DateTimeField(auto_now=True)
    created_lu = models.DateTimeField(auto_now_add=True)
    def detalle(self):
        return "{}, {}, {}".format(self.id_userL, self.id_libroU, self.id_valoracionlu)
    def __str__(self):
        return self.detalle()


    









    
