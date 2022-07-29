from django.shortcuts import render, get_list_or_404, get_object_or_404
#from django.http import HttpResponse
from .models import LivroReceitas


def index(request):
    livros = LivroReceitas.objects.all()

    dados = {
        'livros' : livros
    }
    return render(request, 'index.html',dados)

def receita(request, LivroReceitas_id):
    receita = get_object_or_404(LivroReceitas, pk=LivroReceitas_id)

    receita_a_exibir = {
        'receita' : receita
    }
    return render(request, 'receita.html', receita_a_exibir)