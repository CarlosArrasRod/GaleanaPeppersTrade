from django.shortcuts import render, redirect
from django.http import JsonResponse
from weight.models  import Weight
from vaciado.models  import Vaciado
from calidad.models  import Calidad
from pipas.models  import Pipas
from production.models  import Production
from django.db.models import Q
# Create your views here.
def gerente(request):
    
    if request.user.groups.filter(name='Pipas').exists():
        return redirect('pipas:pipas_list')
    if request.user.groups.filter(name='Vaciado').exists():
        return redirect('vaciado:vaciado')
    if request.user.groups.filter(name='Calidad').exists():
        return redirect('calidad:calidad_lista')
    if request.user.groups.filter(name='Produccion').exists():
        return redirect('production:production_list')
    if request.user.groups.filter(name='Pesos').exists():
        return redirect('weight:weight')
    
    return render(request, 'gerencia/index.html')

def graficas(request, mes, anio):
    # Obtener el año y mes desde la solicitud, por defecto 2024 y octubre (mes 10)
    anio = int(request.GET.get('anio', 2024))  # Obtener el año desde la solicitud
    mes = int(request.GET.get('mes', 9))      # Obtener el mes desde la solicitud

    # Filtrar los registros según el año y mes seleccionados
    weight_records = Weight.objects.filter(pesolib__isnull=False, fecha__year=anio, fecha__month=mes)
    # Obtener las libras y las fechas
    libras = [record.fecha.strftime('%Y-%m-%d') for record in weight_records]  # Formato de fecha
    data = [record.pesolib for record in weight_records]  # Pesos en libras
    ton = [record.pesoton for record in weight_records]
    
    produccion_rec = Production.objects.filter(kgpasta__isnull=False)
    
    tiempo =[ppasta.kgpasta for ppasta in produccion_rec]

    context = {
        'libras': libras,
        'data': data,
        'tiempo': tiempo,
        'ton':ton,
        'anio': anio,
        'mes': mes,
    }

    return render(request, 'gerencia/graficas/graficauno.html', context)

def gerencia_weight(request):
    
    query = request.GET.get('search')  # Obtiene el valor del campo de búsqueda
    if query:
        # Filtra por ID exacto o por coincidencia parcial en el nombre
        weight = Weight.objects.filter(Q(folio__icontains=query) | Q(fecha__icontains=query))
    else:
        # Si no hay búsqueda, muestra todos los registros
        weight = Weight.objects.all()
        
    return render(request, 'gerencia/tablas/g_weight.html', {'weight': weight})

def gerencia_vaciado(request):
    
    query = request.GET.get('search')  # Obtiene el valor del campo de búsqueda
    if query:
        # Filtra por ID exacto o por coincidencia parcial en el nombre
        vaciados = Weight.objects.filter(Q(folio__icontains=query) | Q(fecha__icontains=query))
    else:
        # Si no hay búsqueda, muestra todos los registros
        vaciados = Weight.objects.all()
        
    return render(request, 'gerencia/tablas/g_vaciado.html', {'vaciados': vaciados})

def gerencia_calidad(request):
    query = request.GET.get('search')  # Obtiene el valor del campo de búsqueda
    if query:
        # Filtra por ID exacto o por coincidencia parcial en el nombre
        calidades = Weight.objects.filter(Q(folio__icontains=query))
    else:
        # Si no hay búsqueda, muestra todos los registros
        calidades = Weight.objects.all()
        
    return render(request, 'gerencia/tablas/g_calidad.html', {'calidades': calidades})

def gerencia_production(request):
    
    query = request.GET.get('search')  # Obtiene el valor del campo de búsqueda
    if query:
        # Filtra por ID exacto o por coincidencia parcial en el nombre
        productions = Weight.objects.filter(Q(folio__icontains=query))
    else:
        # Si no hay búsqueda, muestra todos los registros
        productions = Weight.objects.all()
        
    
    
    return render(request, 'gerencia/tablas/g_production.html', {'productions': productions})

def gerencia_pipa(request):
    
    query = request.GET.get('search')  # Obtiene el valor del campo de búsqueda
    if query:
        # Filtra por ID exacto o por coincidencia parcial en el nombre
        pipa = Weight.objects.filter(Q(folio__icontains=query))
    else:
        # Si no hay búsqueda, muestra todos los registros
        pipa = Weight.objects.all()
        
    
    
    return render(request, 'gerencia/tablas/g_pipa.html', {'pipa': pipa})