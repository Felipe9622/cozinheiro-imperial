from django.contrib import admin
from .models import Receita


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')
    list_filter = ['titulo']
    search_fields = ['descricao']
