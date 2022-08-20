from django.contrib import admin
from .models import JobApplication

class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication
    list_display = ('nome_completo', 'email', 'celular', 'criacao')
    exclude = ('session_key',)

admin.site.register(JobApplication, JobApplicationAdmin)