from django.contrib import admin
from mi_app.models import cliente, Activdades_fisicas, Pausas_Activas

# Register your models here.
admin.site.register(cliente)
admin.site.register(Activdades_fisicas)
admin.site.register(Pausas_Activas)