from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail

from .models import Document
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
        if form.is_valid():
            data = form.cleaned_data
			
            msg = EmailMessage(data['subject'],'El cliente: ' + data['name'] + ' Con email: ' + data['email'] + ' Mensaje: ' + data['message'], to=["alpachemi@gmail.com"], fail_silently=False)
            newdoc = Document(docfile = request.FILES['myfile'])
            newdoc.save()
            #myfile = request.FILES['myfile']
            #handle_uploaded_file(request.FILES['file'])
            msg.attach('curriculum.pdf', newdoc, 'application/pdf')
            msg.content_subtype = "html"
            msg.send()
      
            print(data['email'])
            return render(request, 'blog/mensaje.html', {})
    else:
        return render(request, 'blog/trabaja.html', {})

def indexeng(request):
    return render(request, 'blog/indexmanos_eng.html')

def indexfr(request):
    return render(request, 'blog/indexmanos_fr.html')
	
def indexmanos(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                data['subject'],
                'El cliente: ' + data['name'] + ' Con email: ' + data['email'] + ' Mensaje: ' + data['message'],
                data['email'], #FROM
                ['alpachemi@gmail.com'],
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
	
def handle_uploaded_file(f):
    with open('some/file/name.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
	