from django.contrib import admin
from .models import Usuario
from .models import Worker
from .models import Post

admin.site.register(Usuario)
admin.site.register(Worker)
admin.site.register(Post)