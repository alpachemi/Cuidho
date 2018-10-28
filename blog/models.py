from django.db import models
from django.utils import timezone


class Usuario(models.Model):

    #id = models.UUIDField(primary_key=True, help_text="Id para un usuario")
    #nombre = models.ForeignKey('Nombre', on_delete=models.SET_NULL, null=True) 
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(
             blank=False, null=True)
    telefono_1 = models.CharField(max_length=15)
    telefono_2 = models.CharField(max_length=15)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    sexo = models.CharField(max_length=1)
    carne_conducir = models.BooleanField(default=False)
    cuidador = models.BooleanField(default=False)
    administrador = models.BooleanField(default=False)
    password = models.CharField(max_length=100, blank=True, null= True,)
	
    #LOAN_STATUS = (
    #    ('m', 'Maintenance'),
    #    ('o', 'On loan'),
    #    ('a', 'Available'),
    #    ('r', 'Reserved'),
    #)

    def __str__(self):
        return str(self.id)
		
    def publish(self):
        self.save()
		
#class Document(models.Model):
#    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	
class Worker(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    file = models.FileField()
	
    def __str__(self):
        return str(self.id)

class Post(models.Model):
    titulo = models.CharField(max_length=100) 
    subtitulo = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo		
		
		
		