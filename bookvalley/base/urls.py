from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('usuario/', views.usuario),
    path('registro/', views.registro),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('educacionF/', views.mostrarLibros),
    path('superacionP/', views.mostrarLibrosSuperacion),
    path('novelas/', views.mostrarLibrosNovelas),
    path('comunidad/', views.comentarios),
    path('usuario/edicion/<int:id>', views.editar),
    path('editarComentario/', views.editarComentario),
    path('usuario/eliminar/<int:id>', views.eliminar),
    path('busqueda/', views.busqueda),
    path('autores/', views.busquedaAutor),
    path('acerca/', views.acerca)
]