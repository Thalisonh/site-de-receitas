from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recetia

# Create your views here.


def index(request):

    receitas = Recetia.objects.all()

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Recetia, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receita.html', receita_a_exibir)
