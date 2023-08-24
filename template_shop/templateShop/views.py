from django.shortcuts import render, redirect
from .forms import Foto_form

def index(request):
    return render(request, 'index.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def produtos(request):
    return render(request, 'produtos.html')

def adicionar(request):
    form = Foto_form()
    if form.is_valid():
            form.save()
            return redirect('adicionar.html')
    else:
        return