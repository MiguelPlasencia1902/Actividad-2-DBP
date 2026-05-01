from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]