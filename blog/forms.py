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