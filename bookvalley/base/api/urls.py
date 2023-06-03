from django.urls import path
from . import views

urlpatterns=[
    path('', views.routes),
    path('libro/', views.libro),
    path('libro/<int:id>', views.buscarLibro),
    path('autor/', views.autor),
    path('autor/<int:id>', views.buscarAutor)
]