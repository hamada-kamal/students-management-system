from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Complaint, Registraion




admin.site.site_header = "Helwan University"
admin.site.site_title = "Helwan University" 


admin.site.register(Complaint)



# class RegistraionAdmin(admin.ModelAdmin):
#     model = Registraion
#     filter_horizontal = ('subjects',)
    # filter_horizontal = ('categories',)


# admin.site.register(Registraion,RegistraionAdmin)

class RegistraionAdmin(admin.ModelAdmin):
    filter_horizontal = ('subjects', )


# admin.site.unregister(Registraion)
admin.site.register(Registraion, RegistraionAdmin)