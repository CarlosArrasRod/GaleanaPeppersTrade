from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Weight
from .forms import WeightForm

def weight(request):
    #Toda esta funcon es GET
    
    if request.user.groups.filter(name='Pipas').exists():
        return redirect('pipas:pipas_list')
    if request.user.groups.filter(name='Vaciado').exists():
        return redirect('vaciado:vaciado')
    if request.user.groups.filter(name='Calidad').exists():
        return redirect('calidad:calidad_lista')
    if request.user.groups.filter(name='Produccion').exists():
        return redirect('production:production_list')
    if request.user.groups.filter(name='Gerencia').exists():
        return redirect('gerencia:gerente')
    
    
    weight=Weight.objects.all()
    return render(request, 'weight/index.html', {'weight': weight})

def add(request):
    if request.method == 'GET':
        formulario = WeightForm()
    else:
        formulario = WeightForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('../weight/')
    return render(request, 'weight/crear.html', {'formulario': formulario})

def update(request, id):
    weight = Weight.objects.get(id=id)
    formulario = WeightForm(request.POST or None, request.FILES or None, instance=weight)
    if formulario.is_valid():
        formulario.save()
        return redirect('../')
    return render(request, 'weight/editar.html', {'formulario': formulario})

def delete(request, id):
    weight = Weight.objects.get(id=id)
    weight.delete()
    return redirect('/weight')