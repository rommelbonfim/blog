from django.contrib import admin
from .models import*
# Register your models here.
class CamposAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug': ('titulo',)}
admin.site.register(Campos,CamposAdmin)
admin.site.register(Autores)
