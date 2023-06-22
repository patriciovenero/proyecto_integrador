from django.contrib import messages
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
    return render(request, 'index-home.html', context)

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

def login(request):
    if request.method == 'POST':
        correo = request.POST['username']
        clave = request.POST['password']

        try:
            empresa = Empresa.objects.get(correo=correo)
            if empresa.clave == clave:
                # Las credenciales son correctas, realizar alguna acción (por ejemplo, redirigir a otra página)
                return render(request, 'index-principal.html')
            else:
                # La clave es incorrecta, mostrar un mensaje de error
                messages.error(request, 'La clave ingresada es incorrecta.')
        except Empresa.DoesNotExist:
            # No se encontró ninguna empresa con el correo ingresado, mostrar un mensaje de error
            messages.error(request, 'No existe una cuenta asociada a ese correo.')

    return render(request, 'index-login.html')
