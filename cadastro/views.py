from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def cadastros(request):
    
    cadastros = Pessoa.objects.all()

    # realizando a busca e filtrando na tabela
    busca = request.GET.get('search')
    if busca:
        cadastros = Pessoa.objects.filter(nome__icontains=busca)

    return render(request, 'paginas/cadastros.html', {'cadastros': cadastros})


@login_required(login_url='login')
def cadastrar(request):

    form = PessoaForm()
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastros')
    
    context = {'form':form}
    return render(request,'paginas/form_cadastro.html',context)


@login_required(login_url='login')
def detalhe(request, id_pessoa):

    cadastro = Pessoa.objects.get(pk=id_pessoa) 
        
    context = {'cadastro': cadastro}
    return render(request,'paginas/detalhe.html',context)


@login_required(login_url='login')
def editar(request, id_pessoa):

    cadastro = Pessoa.objects.get(pk=id_pessoa)
    
    if request.method == 'GET':
        form = PessoaForm(instance=cadastro)
        context = {'form':form}
        return render(request,'paginas/form_cadastro.html',context)
    else:
        form = PessoaForm(request.POST, instance=cadastro)
        if form.is_valid():
            form.save()
        return redirect('cadastros')


@login_required(login_url='login')
def excluir(request, id_pessoa):

    cadastro = Pessoa.objects.get(pk=id_pessoa)
    
    if request.method == 'POST':
        cadastro.delete()
        return redirect('cadastros')
    return render(request,'paginas/confirmar_exclusao.html',{'form':cadastro})
        








    
   

