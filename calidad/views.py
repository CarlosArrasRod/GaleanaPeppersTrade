from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Calidad, Weight 
from .forms import CalidadForm
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ListaCalidad_ListView(ListView):
    model = Calidad
    template_name = 'calidad/CBV/list.html'
    context_object_name='calidades'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pesos"] = Weight.objects.all()
        return context

class ListaCalidadesPeso_ListView(ListView):
    model = Weight
    template_name = 'calidad/CBV/list_pesoCalidad.html'
    context_object_name = 'pesos'
    

class Agregar_CreateView(CreateView):
    model = Calidad
    template_name = 'calidad/crud/crear.html'
    form_class = CalidadForm
    success_url = reverse_lazy('calidad:calidad_lista')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Obtén el valor del query parameter 'category'
        folio = self.request.GET.get('folio', None)
        if folio:
            # Inicializa el formulario con el valor del query parameter
            kwargs['initial'] = {'weight': Weight.objects.get(folio=folio)}
        return kwargs

class Calidad_detailView(DetailView):
    model = Calidad
    template_name = 'calidad/CBV/detail.html'
    context_object_name = 'calidad'
    



# Create your views here.
def calidad(request):
    
    if request.user.groups.filter(name='Produccion').exists():
        return redirect('production:production_list')
    if request.user.groups.filter(name='Pesos').exists():
        return redirect('weight:weight')
    if request.user.groups.filter(name='Pipas').exists():
        return redirect('pipas:pipas_list')
    if request.user.groups.filter(name='Vaciado').exists():
        return redirect('vaciado:vaciado')
    if request.user.groups.filter(name='Gerencia').exists():
        return redirect('gerencia:gerente')
    
    calidades = Weight.objects.all()
    return render(request, 'calidad/index.html', {'calidades': calidades})




def add(request,w_pk):
    w = Weight.objects.get(id=w_pk)

    if request.method == 'GET':
        formularioc = CalidadForm(
            initial={'weight':w}
            
            )
    else:
        
        formularioc = CalidadForm(data = request.POST)

    if formularioc.is_valid():
        formularioc.save()
        return redirect('calidad:calidad')
    
    
    return render(request, 'calidad/crud/crear.html', {'formularioc': formularioc, 'w':w})
