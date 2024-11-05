from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Pipas, Weight
from .forms import PipasForm
from django.urls import reverse_lazy


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class Agregar_CreateView(CreateView):
    model = Pipas
    template_name='crud/crear.html'
    form_class = PipasForm
    success_url = reverse_lazy('pipas:pipas_list')

    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Obtén el valor del query parameter 'category'
        folio = self.request.GET.get('folio', None)
        if folio:
            # Inicializa el formulario con el valor del query parameter
            kwargs['initial'] = {'weight': Weight.objects.get(folio=folio)}
        return kwargs
    
    def form_valid(self, form):
        return super().form_valid(form)





# Create your views here.
def pipas(request):
    
    if request.user.groups.filter(name='Produccion').exists():
        return redirect('production:production_list')
    if request.user.groups.filter(name='Pesos').exists():
        return redirect('weight:weight')
    if request.user.groups.filter(name='Calidad').exists():
        return redirect('calidad:calidad_lista')
    if request.user.groups.filter(name='Vaciado').exists():
        return redirect('vaciado:vaciado')
    if request.user.groups.filter(name='Gerencia').exists():
        return redirect('gerencia:gerente')
    
    pipa= Weight.objects.all()
    return render(request, 'crud/index.html', {'pipa': pipa})

def add(request,w_pk):
    w = Weight.objects.get(id=w_pk)
    
    
    
    if request.method == 'GET':
        formulariop = PipasForm(
            initial={'weight':w}
            
            )
    else:
        
        formulariop = PipasForm(data = request.POST)
        
    if formulariop.is_valid():
        formulariop.save()
        return redirect('pipas:pipas_list')
    
    return render(request, 'crud/crear.html', {'formulariop': formulariop})

def update(request, id):
    pipas = pipas.objects.get(id=id)
    formulario = PipasForm(request.POST or None, request.FILES or None, instance=pipas)
    formulario.save()
    return render(request, 'pipas/editar.html', {'formulario': formulario})

def delete(request, id):
    pipas = Pipas.objects.get(id=id)
    pipas.delete()
    return redirect('/pipas')