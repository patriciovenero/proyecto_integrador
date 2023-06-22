from django.shortcuts import render
from api.models import *
from .serializers import EmpresaSerializer, EstacionamientoSerializer, EstadoSerializer

# Create your views here.
def index(request):
    lista_empresas = Empresa.objects.all()
    serializer_empresas = EmpresaSerializer(lista_empresas, many=True)

    context = {
        'empresas': serializer_empresas.data,
    }
    return render(request, 'index.html', context)

def estacionamiento(request, nombre):
    lista_estacionamientos = Empresa.objects.filter(nombre=nombre)
    serializer_estacionamientos = EmpresaSerializer(lista_estacionamientos, many=True)

    lista_estados = Estado.objects.all()
    serializer_estados = EstadoSerializer(lista_estados, many=True)

    context = {
        'estacionamientos': serializer_estacionamientos.data,
        'estados': serializer_estados.data,
    }

    return render(request, 'estacionamiento.html', context)
