## 1. Por que escolher Django

Django é um framework que já utilizei antes e quero me aprofundar e relembrar alguns conceitos. Ele é amplamente usado no mercado de trabalho por sua facilidade e por trazer diversas funcionalidades nativas, economizando tempo e linhas de código. É um framework orientado a conteúdo, facilita operações de CRUD, possui ORM nativo, uma interface administrativa excelente e fácil de customizar, utiliza a arquitetura MVT (Model, View, Template) e, por fim, é muito seguro. Tratar segurança com Django é mais simples do que em outros frameworks.

Vamos começar!

---

## 2. Começando o projeto Django

Para iniciar o projeto, instale o `virtualenv` e o Django. **Lembre-se:** instale o Django apenas dentro do ambiente virtual, não diretamente na sua máquina.

```bash
django-admin startproject setup .
```

É comum ver projetos com o nome `setup`, pois essa pasta contém todas as configurações do projeto. O ponto final evita que o Django crie uma subpasta com o mesmo nome.

---

## 3. Rodando o servidor

Para visualizar o projeto rodando, execute:

```bash
python manage.py runserver
```

Após esse comando, aparecerá um endereço como http://127.0.0.1:8000. Segure `CTRL` e clique para acessar o projeto rodando localmente.

---

## 4. Variáveis de ambiente e sua importância

Variáveis de ambiente são usadas para armazenar dados sensíveis, como chaves de acesso e senhas, que não devem ser expostos. Elas ficam em um arquivo chamado `.env`. Para ler esse arquivo no Django, instale a biblioteca:

```bash
pip install python-dotenv
```

No arquivo `setup/settings.py`, adicione:

```python
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
```

Remova a `SECRET_KEY` do `settings.py` e coloque no `.env`:

```env
SECRET_KEY=sua_SECRET_KEY
```

Para carregar a chave no `settings.py`:

```python
SECRET_KEY = str(os.getenv('SECRET_KEY'))
```

**Importante:** Para evitar que o `.env` seja enviado ao GitHub, adicione-o ao `.gitignore`. Use o site [gitignore.io](https://www.toptal.com/developers/gitignore) para gerar um arquivo adequado para Python/Django.

> **Atenção:** O nome do arquivo `.gitignore` deve estar correto. Qualquer erro impede que o Git ignore os arquivos desejados.

---

## 5. Django Apps

No Django, cada nova funcionalidade é criada como um "app". Por exemplo, para adicionar clientes:

```bash
python manage.py startapp clientes
```

Isso cria uma pasta `clientes/` para toda a lógica desse app.

Estrutura típica do projeto:

```
📂 clientes/
📂 setup/
📂 venv/
📄 .env
📄 .gitignore
📄 db.sqlite3
📄 manage.py
📄 Readme.md
📄 requirements.txt
```

Para registrar o app, adicione-o em `INSTALLED_APPS` no `setup/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientes',
]
```

---

## 6. Models e Views

### Views

Views exibem informações do app. Exemplo de view simples:

```python
# clientes/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Título</h1>')
```

No arquivo de URLs principal:

```python
# setup/urls.py
from django.contrib import admin
from django.urls import path
from clientes.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
```

---

## 7. Isolando URLs dos Apps

Para projetos com muitos apps, isole as URLs de cada app em um arquivo próprio. Exemplo:

```python
# clientes/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
]
```

No arquivo principal de URLs:

```python
# setup/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),
]
```

---

## 8. Models

Models são classes Python que representam tabelas do banco de dados. Exemplo:

```python
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
```

---

## 9. Migrations

Migrations criam e alteram tabelas no banco de dados conforme os models definidos.

- **Criar migration:**
  ```bash
  python manage.py makemigrations
  ```
- **Aplicar migration:**
  ```bash
  python manage.py migrate
  ```
- **Ver status das migrations:**
  ```bash
  python manage.py showmigrations
  ```

---

## 10. ORM

O ORM (Object-Relational Mapping) permite interagir com o banco de dados usando objetos Python, sem precisar escrever SQL diretamente. Cada model representa uma tabela, cada atributo representa uma coluna e cada instância representa uma linha.

---

## 11. Django Admin

O Django Admin é uma interface administrativa pronta para gerenciar os dados da aplicação. Após definir os models e aplicar as migrations, acesse `/admin` para visualizar e manipular os dados.

Para acessar o admin, crie um superusuário:

```bash
python manage.py createsuperuser
```

Preencha os dados solicitados e, depois, rode o servidor:

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) usando o usuário e senha cadastrados.

---

## 12. Persistência de Imagens no Amazon S3

O Amazon S3 (Simple Storage Service) é um serviço de armazenamento em nuvem da AWS, muito utilizado para guardar arquivos como imagens, vídeos e documentos de forma segura, escalável e acessível pela internet. Utilizar o S3 para armazenar imagens em projetos Django é uma prática comum, pois evita o uso do armazenamento local do servidor e facilita o gerenciamento dos arquivos.

### O que é o S3?

O S3 é um serviço de armazenamento de objetos, onde você pode criar "buckets" (pastas virtuais) para guardar seus arquivos. Ele oferece alta disponibilidade, segurança e integração com diversos serviços da AWS.

---

### Como criar uma conta na AWS e um bucket S3

1. **Criar uma conta AWS:**
   - Acesse [aws.amazon.com](https://aws.amazon.com/) e clique em "Criar uma conta gratuita".
   - Siga os passos de cadastro, incluindo informações de pagamento (há um plano gratuito com limites).

2. **Criar um bucket S3:**
   - No console da AWS, procure por "S3" e acesse o serviço.
   - Clique em "Criar bucket".
   - Dê um nome único ao bucket e escolha a região desejada.
   - Mantenha as configurações padrão ou ajuste conforme sua necessidade.
   - Finalize a criação.

3. **Criar um usuário IAM para acesso programático:**
   - No console da AWS, acesse "IAM" > "Usuários" > "Adicionar usuário".
   - Defina um nome e selecione "Acesso programático".
   - Anexe a política "AmazonS3FullAccess" (ou uma política personalizada com permissões restritas ao bucket).
   - Salve as credenciais (Access Key ID e Secret Access Key).

---

### Como aplicar e configurar no Django

1. **Instalar a biblioteca de integração:**

   No ambiente virtual do seu projeto, instale o pacote `django-storages` e o `boto3`:

   ```bash
   pip install django-storages boto3
   ```

2. **Configurar o Django para usar o S3:**

   No arquivo `settings.py`, adicione as seguintes configurações:

   ```python
   # settings.py

   INSTALLED_APPS += ['storages']

   # Configurações do S3
   AWS_ACCESS_KEY_ID = 'SUA_ACCESS_KEY_ID'
   AWS_SECRET_ACCESS_KEY = 'SUA_SECRET_ACCESS_KEY'
   AWS_STORAGE_BUCKET_NAME = 'nome-do-seu-bucket'
   AWS_S3_REGION_NAME = 'sua-regiao'  # Exemplo: 'us-east-1'
   AWS_QUERYSTRING_AUTH = False

   DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
   ```

   > **Dica:** Para maior segurança, armazene as credenciais no arquivo `.env` e carregue-as usando `os.getenv()`.

3. **Salvar arquivos no S3:**

   Com essa configuração, qualquer arquivo enviado por um `ImageField` ou `FileField` será automaticamente salvo no S3.

---

### Exemplo de uso em um model

```python
from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='fotos/')
    # outros campos...
```

Ao adicionar ou atualizar imagens pelo Django Admin ou formulários, os arquivos serão enviados diretamente para o S3.

---

## Referências

- [Documentação oficial do Django (pt-br)](https://docs.djangoproject.com/pt-br/)
- [Guia de boas práticas com Django](https://www.djangoproject.com/)
- [gitignore.io](https://www.toptal.com/developers/gitignore)
- [Documentação oficial do django-storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
- [Documentação oficial do Amazon S3](https://docs.aws.amazon.com/pt_br/s3/index.html)
- [Guia rápido AWS S3](https://docs.aws.amazon.com/pt_br/AmazonS3/latest/gsg/GetStartedWithS3.html)


---

## Resumo

Este projeto apresenta os fundamentos básicos do Django, incluindo criação de projetos, apps, views, models, migrations, uso de variáveis de ambiente, ORM e Django Admin. Para se aprofundar, consulte a documentação oficial e pratique criando novos apps e funcionalidades!


