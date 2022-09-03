from django.contrib import admin
from .models import Usuario, Lista, Item

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Lista)
admin.site.register(Item)