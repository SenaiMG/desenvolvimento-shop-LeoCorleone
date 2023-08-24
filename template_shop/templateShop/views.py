from django.shortcuts import render, redirect
from .forms import Foto_form

def index(request):
    return render(request, 'index.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def produtos(request):
    return render(request, 'produtos.html')

def adicionar(request):
    form = Foto_form(request)
    context = {'form': form}
    return render(request, 'index.html', context)