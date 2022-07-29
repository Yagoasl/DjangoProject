from django.contrib import admin
from .models import LivroReceitas

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita','categoria','tempo_de_preparo')
    list_display_links = ('id', 'nome_receita')

admin.site.register(LivroReceitas, ListandoReceitas)

#loguin localhost:8000/admin
#user = admin
#pass = 123456