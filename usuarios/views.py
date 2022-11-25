from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def novo_usuario(request):
    formulario = UserRegisterForm()

    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = formulario.cleaned_data.get('username')
            messages.success(request, f'Usuário {user} criado com sucesso')
            return redirect('login')

    context = {'formulario':formulario}
    return render(request, 'usuarios/registrar.html', context)


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cadastros')
        else:
            messages.info(request, 'Usuário ou Senha incorretos')

    context = {}
    return render(request, 'usuarios/login.html', context)


def logoutUsuario(request):
    logout(request)
    return redirect('login')






