from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/adicionar_livro.html', {'form': form})

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})

def marcar_lido(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.lido = True
    livro.save()
    return redirect('listar_livros')

def remover_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('listar_livros')
