
from django.views.generic import TemplateView

from django.shortcuts import redirect




class dashboard(TemplateView):
    """
    como en el settings.py esta configurado el "LOGIN_REDIRECT_URL = 'dashboard'"
    al entrar a esta view, lera el request.user y ahora si lo 
    redirecciona segun su group
    """
    template_name = 'weight/dashboard.html'
    def get(self, request, *args, **kwargs):        
        
        if request.user.is_authenticated:
        
            if request.user.groups.filter(name='Pipas').exists():
                return redirect('pipas:pipas_list')
            elif request.user.groups.filter(name='Pesos').exists():
                return redirect('weight:weight')
            elif request.user.groups.filter(name='Vaciado').exists:
                return redirect('vaciado:vaciado')
            elif request.user.groups.filter(name='Produccion').exists:
                return redirect('production:production_list')
            elif request.user.groups.filter(name='Calidad').exists:
                return redirect('calidad:calidad_lista')
            elif request.user.groups.filter(name='Gerencia').exists():
                return redirect('gerencia:gerente')
        else:
            return redirect('account_login')  # si no esta logeado redirecciona al login
        return super().get(request, *args, **kwargs)