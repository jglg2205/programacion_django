from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Libro, Autor_libro, Valoracion, Genero, Genero_libro, Libro_usuario, Autor

# Create your views here.

def home(request):
    contenido = Autor_libro.objects.all()
    return render(request, 'home.html', {'autor':contenido})

def usuario(request):
    valoracion = Valoracion.objects.all()
    return render(request, 'usuario.html',{'valoracion':valoracion})


def registro(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/registro')
        User.objects.create_user(username = username, email = email, first_name = name, last_name = last_name, password = password)
        messages.success(request, 'Registro Exitoso')
        return redirect('/')

    return render(request, 'registro.html')

def loginPage(request):
    if (request.method =='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de Sesion Exitoso')
                return redirect('/usuario')
        messages.error(request, 'Datos incorrectos')
    return render (request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/')

def mostrarLibros(request):
    libros = Genero_libro.objects.filter(id_generoL=1).order_by('id_libroG')

    if (request.method =='POST'):
        
        comentario = request.POST.get('comentario')
        puntos = request.POST.get('puntos')
        user = request.user
        id_libroV= request.POST.get('id_libroV')
        libro=Libro.objects.get(id=id_libroV)
        n = Valoracion.objects.create(comentario=comentario, puntos=puntos, user=user, id_libroV=libro)
        busqueda= n.id
        id_val= Valoracion.objects.get(id=busqueda)
        Libro_usuario.objects.create(id_userL=user, id_libroU=libro, id_valoracionlu= id_val)
        messages.success(request, 'Gracias por tu opinion')

    return render (request, 'educacionF.html',{'libros':libros})

def mostrarLibrosSuperacion(request):
    libros_S = Genero_libro.objects.filter(id_generoL=2).order_by('id_libroG')
    if (request.method =='POST'):
        comentario = request.POST.get('comentario')
        puntos = request.POST.get('puntos')
        user = request.user
        id_libroV= request.POST.get('id_libroV')
        libroS=Libro.objects.get(id=id_libroV)
        n= Valoracion.objects.create(comentario=comentario, puntos=puntos, user=user, id_libroV=libroS)
        busqueda= n.id
        id_val= Valoracion.objects.get(id=busqueda)
        Libro_usuario.objects.create(id_userL=user, id_libroU=libroS, id_valoracionlu= id_val)
        messages.success(request, 'Gracias por tu opinion')
        
    return render (request, 'superacionP.html',{'libros_S': libros_S})

def mostrarLibrosNovelas(request):
    libros_N = Genero_libro.objects.filter(id_generoL=3).order_by('id_libroG')
    if (request.method =='POST'):
        comentario = request.POST.get('comentario')
        puntos = request.POST.get('puntos')
        user = request.user
        id_libroV= request.POST.get('id_libroV')
        libroN=Libro.objects.get(id=id_libroV)
        n =Valoracion.objects.create(comentario=comentario, puntos=puntos, user=user, id_libroV=libroN)
        busqueda = n.id
        id_val= Valoracion.objects.get(id=busqueda)
        Libro_usuario.objects.create(id_userL=user, id_libroU=libroN, id_valoracionlu= id_val)
        messages.success(request, 'Gracias por tu opinion')
        

    return render (request, 'novelas.html',{'libros_N': libros_N})

def comentarios(request):
    
    comentario = Libro_usuario.objects.all()
    return render(request, 'comentarios.html', {'comentario':comentario})

def editar(request, id):
    publicacion = Valoracion.objects.get(id=id)
    return render(request, 'edicion.html', {'publicacion':publicacion})

def eliminar(request, id):
    opinion = Valoracion.objects.get(id=id)
    opinion.delete()
    messages.success(request, 'Publicacion eliminada con exito')
    return redirect('/usuario')

def editarComentario(request):
   id= request.POST.get('id')
   comentario=request.POST.get('comentario')
   puntos=request.POST.get('puntos')
   user =request.user
   id_libroV = request.POST.get('id_libroV')
   libro =Libro.objects.get(id=id_libroV)
   publicacion = Valoracion.objects.get(id=id)
   publicacion.comentario = comentario
   publicacion.puntos = puntos
   publicacion.user = user
   publicacion.id_libroV = libro
   publicacion.save()
   messages.success(request, 'Comentario editado con exito')
   return redirect('/usuario')

def busqueda(request):
    if(request.method == 'GET'):
        queryset = request.GET.get('buscar')
        datos =Libro.objects.all()
        if queryset:
            datos = Libro.objects.filter(
                Q(titulo_libro__icontains = queryset)
            ).distinct()
    return render(request, 'busqueda.html',{'datos':datos})

def busquedaAutor(request):
    if(request.method == 'GET'):
        queryset = request.GET.get('buscar')
        datos =Autor.objects.all()
        if queryset:
            datos = Autor.objects.filter(
                Q(nombre_autor__icontains = queryset) |
                Q(apellido_autor__icontains = queryset)
            ).distinct()
    return render(request, 'autores.html',{'datos':datos})

def acerca(request):
    valor = Valoracion.objects.filter(puntos='5')
    return render(request,'acerca.html',{'valor':valor})
