from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Estacionamiento(models.Model):
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=255)

    def __str__(self):
        return f"Estacionamiento {self.lugar}"

class Estado(models.Model):
    id_estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        if self.estado == True:
            return f"Estado: {self.estado} ocupado - Ingreso: {self.hora_ingreso}"
        else:
            return f"Estado: {self.estado} desocupado - Salida: {self.hora_salida}"
