from django.contrib import admin
from.models import programmer, Student

# Register your models here.

admin.site.register(programmer)#se registra el modelo para poder verlo en el panel de administracion.
admin.site.register(Student)

