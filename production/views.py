from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Production, Weight
from .forms import ProductionForm
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class Agregar_CreateView(CreateView):
    model = Production
    template_name='production/crud/crear.html'
    form_class = ProductionForm
    success_url = reverse_lazy('production:production_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Obtén el valor del query parameter 'category'
        folio = self.request.GET.get('folio', None)
        if folio:
            # Inicializa el formulario con el valor del query parameter
            kwargs['initial'] = {'weight': Weight.objects.get(folio=folio)}
        return kwargs
    
class Update_UpdateView(UpdateView):
    model = Production
    template_name='production/crud/editar/<int:pk>'
    form_class = ProductionForm
    success_url = reverse_lazy('production:production')
    
    


# Create your views here.
def production(request):
    
    if request.user.groups.filter(name='Pipas').exists():
        return redirect('pipas:pipas_list')
    if request.user.groups.filter(name='Pesos').exists():
        return redirect('weight:weight')
    if request.user.groups.filter(name='Calidad').exists():
        return redirect('calidad:calidad_lista')
    if request.user.groups.filter(name='Vaciado').exists():
        return redirect('vaciado:vaciado')
    if request.user.groups.filter(name='Gerencia').exists():
        return redirect('gerencia:gerente')
    
    productions=Weight.objects.all()
    return render(request, 'production/index.html', {'productions': productions})

def update(request, id):
    production = Production.objects.get(id=id)
    w = production.weight
    
    if request.method == 'GET':                
        formulariov = ProductionForm(instance=production)
    
    if request.method == 'POST':
        formulariov = ProductionForm(request.POST or None, request.FILES or None, instance=production)
        if formulariov.is_valid():
            formulariov.save()
        return redirect('production:production')

    context ={
        'formulariov': formulariov, 
        'w':w,
        'production':production
        }
    return render(request, 'production/crud/editar.html', context)

def delete(request, id):
    productions = Production.objects.get(id=id)
    productions.delete()
    return redirect('production:production_list')