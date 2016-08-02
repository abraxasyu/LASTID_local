from django.contrib import admin
from .models import nextid
# Register your models here.
class nextidadmin(admin.ModelAdmin):
    readonly_fields = ('nextid_time',)

admin.site.register(nextid,nextidadmin)