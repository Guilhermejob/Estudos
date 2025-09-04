from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form['username'].value()
            senha = form['password'].value()
            
        usuario = auth.authenticate(
            request=request,
            username=nome,
            password=senha
        )
        
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Usuario logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Usuario ou senha invalidos')
            return redirect('login')
            
            
            
            
    
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):

    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form['password'].value() != form['confirm_password'].value():
                messages.error(request, 'Senhas são diferentes')
                return redirect('cadastro')
            
            nome = form['username'].value()
            email = form['email'].value()
            senha = form['password'].value()
            
            if User.objects.filter(username = nome).exists():
                messages.error(request, 'Usuario ja existe')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            
            usuario.save()
            messages.success(request, 'Usuario cadastrado com sucesso!')
            return redirect('login')
                        
    
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    
    messages.success(request, 'Usuario deslogado com sucesso!')
    
    return redirect('login')