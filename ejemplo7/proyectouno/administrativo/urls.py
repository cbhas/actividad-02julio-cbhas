
from django.urls import path
# se importa las vistas de la aplicación
from administrativo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-estudiante/', views.crear_estudiante, name='crear_estudiante'),
    path('crear-modulo/', views.crear_modulo, name='crear_modulo'),
    path('modulos/', views.ver_modulos, name='ver_modulos'),
    path('detalle-estudiante/<int:id>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('detalle-matricula/<int:id>/', views.detalle_matricula, name='detalle_matricula'),
    path('crear-matricula/', views.crear_matricula, name='crear_matricula'),
    path('editar-matricula/<int:id>/', views.editar_matricula, name='editar_matricula'),
    path('ver-estudiantes/', views.ver_estudiantes, name='ver_estudiantes'),
]
