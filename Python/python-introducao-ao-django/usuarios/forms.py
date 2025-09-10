from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(
        label='Nome de Usuário', 
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nome de Usuário'
            }    
        ), 
    )
    
    password = forms.CharField(
        label='Senha', 
        max_length=70, 
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Senha'
            }    
        ), 
    )
    
class CadastroForms(forms.Form):
    username = forms.CharField(
        label='Nome de Cadastro', 
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'EX.: João da Silva'
            }    
        ), 
    )
    
    email = forms.EmailField(
        label='E-mail',
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'EX.: joaos@email.com',
            }
        ),
    )
    
    password = forms.CharField(
        label='Senha', 
        max_length=70, 
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }    
        ), 
    )
    
    confirm_password = forms.CharField(
        label='Repita sua senha', 
        max_length=70, 
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirme sua senha'
            }    
        ), 
    )
    
    def clean_username(self):
        nome = self.cleaned_data.get('username')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Nome de usuário não pode conter espaços.')
            else:
                return nome
            
    def clean_password(self):
        senha = self.cleaned_data.get('password')
        senha2 = self.cleaned_data.get('confirm_password')

        if senha and senha2:
            if senha2 != senha2:
                raise forms.ValidationError('As senhas não são iguais.')
            else:
                return senha
    
            