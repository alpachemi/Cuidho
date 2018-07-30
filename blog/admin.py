from django.contrib import admin
from .models import Usuario
from .models import Worker

admin.site.register(Usuario)
admin.site.register(Worker)