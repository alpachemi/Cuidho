from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Worker
from .models import Usuario
from .forms import UsuarioForm
from .forms import LoginForm
from .forms import ContactForm
from .forms import WorkForm
 
	
# Create your views here.

def thanks(request):
    return render(request, 'blog/mensaje.html')

def trabaja(request):
    if request.method == 'POST':

        form = WorkForm(request.POST)
        if form.is_valid() and ('filepath' in request.FILES):
            data = form.cleaned_data
            #worker = form.save(commit=False)
          #   worker.subject = data['subject']
          #   worker.name = data['name']
          #   worker.email = data['email']
           # worker.save()
			
           #  msg = EmailMessage(data['subject'],'El cliente: ' + data['name'] + ' Con email: ' + data['email'] + ' Mensaje: ' + data['message'] + ' Telefono: ' + data['phone'], to=["alpachemi@gmail.com"], fail_silently=False)
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)
            send_mail(
                'Bolsa de trabajo','Asunto: '+ data['subject'] + 
                ' El Trabajador: ' + data['name'] + ' Con email: ' + data['email'] + ' Mensaje: ' + data['message'] + ' Telefono: ' + data['phone'],
                data['email'], #FROM
                ['info@manospararespirar.com'],
                fail_silently=False,
            )
      
            print(data['email'])		
            return render(request, 'blog/mensaje.html', {})
        else:
            if form.is_valid():
                data = form.cleaned_data
                send_mail(
                'Bolsa de trabajo','Asunto: '+ data['subject'] + 
                ' El Trabajador: ' + data['name'] + ' Con email: ' + data['email'] + ' Mensaje: ' + data['message'] + ' Telefono: ' + data['phone'],
                data['email'], #FROM
                ['info@manospararespirar.com'],
                fail_silently=False,
                 )
                print(data['email'])		
                return render(request, 'blog/mensaje.html', {})
 
            else:
                print('ERROR')
                return render(request, 'blog/mensaje.html', {})
 
    else:
        form = WorkForm()
        return render(request, 'blog/trabaja.html', {'form': form})

def indexeng(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                'Cliente','Asunto: '+ data['subject'] + 
                ' El cliente: ' + data['name'] + ' Con email: ' + data['email'] + ' Mensaje: ' + data['message'] + ' Telefono: ' + data['phone'],
                data['email'], #FROM
                ['info@manospararespirar.com'],
                fail_silently=False,
            )
      
            print(data['email'])
            return render(request, 'blog/mensaje.html', {})
    else:
        return render(request, 'blog/indexmanos_eng.html', {})
 
def indexfr(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                'Cliente','Asunto: '+ data['subject'] + 
                ' El cliente: ' + data['name'] + ' Con email: ' + data['email'] + ' Mensaje: ' + data['message'] + ' Telefono: ' + data['phone'],
                data['email'], #FROM
                ['info@manospararespirar.com'],
                fail_silently=False,
            )
      
            print(data['email'])
            return render(request, 'blog/mensaje.html', {})
    else:
        return render(request, 'blog/indexmanos_fr.html', {})
 
	
def indexmanos(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                'Cliente','Asunto: '+ data['subject'] + 
                ' El cliente: ' + data['name'] + ' Con email: ' + data['email'] + ' Mensaje: ' + data['message'] + ' Telefono: ' + data['phone'],
                data['email'], #FROM
                ['info@manospararespirar.com'],
                fail_silently=False,
            )
      
            print(data['email'])
            return render(request, 'blog/mensaje.html', {})
    else:
        return render(request, 'blog/indexmanos.html', {})
 
	
def registro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            # usuario.nombre = form.fields.nombre
            # usuario.apellidos = form.apellidos
            # usuario.telefono_1 = form.telefono_1
            # usuario.telefono_2 = form.telefono_2
            # usuario.provincia = form.provincia
            # usuario.localidad = form.localidad
            # usuario.direccion = form.direccion
            # usuario.telefono_2 = form.telefono_2
            # usuario.codigo_postal = form.codigo_postal
            # usuario.carne_conducir = form.carne_conducir
            # usuario.sexo = form.sexo
            # usuario.cuidador = form.cuidador
            # usuario.administrador = False
            # usuario.fecha_nacimiento = form.fecha_nacimiento
			
            # email = form.email
            # email = email.lower().strip() # Hopefully reduces junk to ""
            # if email != "": # If it's not blank
                # if not email_re.match(email): # If it's not an email address
                    # raise ValidationError(u'%s is not an email address, dummy!' % email)
            # if email == "":
                # email = None
            # usuario.email = email
            usuario.save()

            return redirect('blog/post_list.html', pk=usuario.pk)
    else:
        form = UsuarioForm()
    return render(request, 'blog/registro.html', {'form': form})