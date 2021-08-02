from django.contrib import admin
from .models import Subject, Level, Lecture
# Register your models here.

admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Lecture)
