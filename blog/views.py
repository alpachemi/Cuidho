from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from .models import Post
from .models import Usuario
from .forms import UsuarioForm
from .forms import LoginForm

# Create your views here.
def post_list(request):
    print("Esto va")
    if request.method == 'POST': 
       form = LoginForm(request.POST)
       if form.is_valid():
          email = form.cleaned_data['email']
          print(email)
          password = form.cleaned_data['password']
          user = authenticate(email=email, password=password)
       #user = Usuario.objects.get(email = email)
          if user is not None:
            print("Esto va")
            login(request, user)
          else:
            print("Usario no reconocido")
            form = LoginForm()		 
    else:
       form = LoginForm()
			
    return render(request, 'blog/indexmanos.html', {'form': form})
	
def ofertas(request):
    return render(request, 'blog/blog_right_sidebar.html', {})
def mision(request):
    return render(request, 'blog/mision.html', {})
def vision(request):
    return render(request, 'blog/vision.html', {})
def index(request):
    return render(request, 'blog/index.html', {})
def indexmanos(request):
    if request.method == "POST":
        
        #usuario = request.POST.__getitem__(name)	 
        #print(usuario)
        print("BENNE")
        # send_mail(
        # 'Subject here',
        # 'Here is the message.',
        # 'from@example.com',
        # ['alpachemi@gmail.com'],
        # fail_silently=False,
        # )
        return render(request, 'blog/indexmanos.html', {})
			
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
	
#def indexlog(request):
#    return render(request, 'blog/vision.html', {})
