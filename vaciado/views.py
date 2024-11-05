from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Vaciado, Weight
from .forms import VaciadoForm
# Create your views here.
def vaciado(request):
    
    if request.user.groups.filter(name='Pipas').exists():
        return redirect('pipas:pipas_list')
    if request.user.groups.filter(name='Pesos').exists():
        return redirect('weight:weight')
    if request.user.groups.filter(name='Calidad').exists():
        return redirect('calidad:calidad_lista')
    if request.user.groups.filter(name='Produccion').exists():
        return redirect('production:production_list')
    if request.user.groups.filter(name='Gerencia').exists():
        return redirect('gerencia:gerente')
    
    vaciados = Weight.objects.all()
    return render(request, 'vaciado/index.html', {'vaciados': vaciados})




def add(request,w_pk):
    w = Weight.objects.get(id=w_pk)

    if request.method == 'GET':
        formulariov = VaciadoForm(
            initial={'weight':w}
            
            )
    else:
        #aqui cuando se hace submit al form ya viene el papa osea 
        # weight ya viene en el post data, no es necesario instancarlo por que no hay 
        #instancia de vaciado con el numero del papa. 
        formulariov = VaciadoForm(data = request.POST)

    if formulariov.is_valid():
        formulariov.save()
        return redirect('vaciado:vaciado')
    
    
    return render(request, 'vaciado/crud/crear.html', {'formulariov': formulariov, 'w':w})

def update(request, id):
    vaciado = Vaciado.objects.get(id=id)
    w = vaciado.weight
    
    if request.method == 'GET':                
        formulariov = VaciadoForm(instance=vaciado)
    
    if request.method == 'POST':
        formulariov = VaciadoForm(request.POST or None, request.FILES or None, instance=vaciado)
        if formulariov.is_valid():
            formulariov.save()
        return redirect('vaciado:vaciado')

    context ={
        'formulariov': formulariov, 
        'w':w,
        'vaciado':vaciado
        }
    return render(request, 'vaciado/crud/editar.html', context)


def delete(request, id):
    vaciado = vaciado.objects.get(id=id)
    vaciado.delete()
    return redirect('/vaciado/crud')