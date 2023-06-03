from django.http import JsonResponse
from ..models import Libro, Autor

def routes(request):
    routes=[
        'GET /api/libro',
        'GET /api/libro/:id',
        'GET /api/autor',
        'GET /api/autor/:id'
    ]
    return JsonResponse(routes, safe=False)

def libro(request):
    libro= Libro.objects.all()
    libro_dic =[]
    for l in libro:
        libro_dic.append(
            {
                'titulo':l.titulo_libro,
                'descripcion': l.descripcion_libro
            }
        )
    return JsonResponse(libro_dic, safe=False)

def buscarLibro(request, id):
    buscar = Libro.objects.get(id=id)
    libro_dic=[
        {
         'id':buscar.id,
         'titulo':buscar.titulo_libro,
         'descripcion': buscar.descripcion_libro}
    ]
    return JsonResponse(libro_dic, safe=False)


def autor(request):
    autor= Autor.objects.all()
    autor_dic =[]
    for l in autor:
        autor_dic.append(
            {
                'nombre':l.nombre_autor,
                'apellido': l.apellido_autor,
                'biografia': l.biografia
            }
        )
    return JsonResponse(autor_dic, safe=False)

def buscarAutor(request, id):
    buscar = Autor.objects.get(id=id)
    libro_dic=[
        {
         'id':buscar.id,
         'titulo':buscar.nombre_autor,
         'descripcion': buscar.apellido_autor,
         'biografia': buscar.biografia
         }
    ]
    return JsonResponse(libro_dic, safe=False)

