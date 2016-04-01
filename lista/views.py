from django.shortcuts import render

# Create your views here.

#EDITAR
def producto(request):
    return render(request, 'producto/proc.html', {})