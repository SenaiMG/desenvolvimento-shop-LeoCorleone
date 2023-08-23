from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def produtos(request):
    return render(request, 'produtos.html')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})