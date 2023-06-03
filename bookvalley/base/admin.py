from django.contrib import admin

# Register your models here.

from .models import Libro, Autor, Autor_libro, Genero, Genero_libro, Valoracion, Libro_usuario


admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Autor_libro)
admin.site.register(Genero)
admin.site.register(Genero_libro)
admin.site.register(Valoracion)
admin.site.register(Libro_usuario)
