from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto

# Listar autos
def index(request):
    autos = Auto.objects.all()
    return render(request, 'listar_autos.html', {'autos': autos})

# Ver auto (opcional, puedes usarlo si quieres detalle)
def ver_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'ver_auto.html', {'auto': auto})

# Agregar auto
def agregar_auto(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        año = request.POST['año']
        color = request.POST['color']
        Auto.objects.create(marca=marca, modelo=modelo, año=año, color=color)
        return redirect('inicio')  # Redirige al listado de autos
    return render(request, 'agregar_auto.html')

# Editar auto
def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.marca = request.POST['marca']
        auto.modelo = request.POST['modelo']
        auto.año = request.POST['año']
        auto.color = request.POST['color']
        auto.save()  # Guarda los cambios
        return redirect('inicio')  # Redirige al listado de autos
    return render(request, 'editar_auto.html', {'auto': auto})

# Borrar auto
def borrar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()  # Elimina el auto de la base de datos
        return redirect('inicio')  # Redirige al listado de autos
    return render(request, 'borrar_auto.html', {'auto': auto})
