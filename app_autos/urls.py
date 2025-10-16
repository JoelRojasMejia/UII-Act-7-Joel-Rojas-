from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_auto, name='ver_auto'),
    path('agregar/', views.agregar_auto, name='agregar_auto'),
    path('editar/<int:id>/', views.editar_auto, name='editar_auto'),
    path('borrar/<int:id>/', views.borrar_auto, name='borrar_auto'),
]
