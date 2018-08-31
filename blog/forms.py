from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
          #  if field.Label != "Fecha Nacimiento":
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
		#	else:
		#		self.fields[field].widget.attrs.update({
         #           'class': 'form-control'
         #       })
			
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellidos','fecha_nacimiento','telefono_1','telefono_2','email','provincia','localidad','direccion','codigo_postal','sexo','carne_conducir','cuidador','password',)	
		
class LoginForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput()) 
    #email = forms.EmailField(max_length=70)
    
    class Meta:
       model = Usuario
       fields = ('email', 'password',)	

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

class WorkForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    surname = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    phone = forms.CharField(max_length=25)
    message = forms.CharField(widget=forms.Textarea)
    dni = forms.CharField(max_length=25)
    ciudad = forms.CharField(max_length=25)
    edad = forms.CharField(max_length=25)
    nacionalidad = forms.CharField(max_length=55)
    #experiencia
    formacion = forms.CharField(max_length=200)
    especifica = forms.CharField(max_length=200)
    cuidados = forms.CharField(max_length=5)
    remunerados = forms.CharField(max_length=5)
    duracion = forms.CharField(max_length=25)
    #tipo
    dependencia = forms.CharField(max_length=5)
    parcial = forms.CharField(max_length=5)
    acompanamiento = forms.CharField(max_length=5)
    #disponibilidad
    interno = forms.CharField(max_length=5)
    media_jornada = forms.CharField(max_length=5)
    #sustituciones
    entre_semana = forms.CharField(max_length=5)
    fines_semana = forms.CharField(max_length=5)
    #desplazamiento
    vehiculo = forms.CharField(max_length=5)
    desplazamiento = forms.CharField(max_length=25)
    solo_localidad = forms.CharField(max_length=5)
    provincia = forms.CharField(max_length=5)
	