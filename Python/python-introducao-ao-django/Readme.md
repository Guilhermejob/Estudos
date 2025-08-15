## 1. Por que escolher Django

primeiro e um framework que já trabalhei antes, quero me aprofundar nele e relembrar algumas coisas, segundo que ele é amplamente usado no mercado de trabalho por sua facilidade de ter varias coisas já nativamente nele, então em resumo, se economiza tempo e linhas de código, e um framework orientado a conteudo, operações de CRUD são facilitadas usando essa ferramenta, possui ORM nativo, a interface dele de ADM é fantastica, com muitas opções ja prontas e outras faceis de implementar, usa a arquitetura MVT(model, view, template), e por ultimo mas não menos importante, e um framework muito seguro, para tratar de segurança com o Django é relativamente mais facil que com outros frameworks, então vamos la!

para começarmos o projeto iremos instalar de cara o virtualenv e o django, LEMBRE-SE: o django só vai ser instalado após estivermos dentro do ambiente virtual, e nao na sua maquina

### 2. Começando nosso projeto no Django

o django nos da uma facilidade incrivel, com 1 comando ele nos entrega toda a estrutura de configurações que precisamos para iniciarmos nosso projeto e esse comando é

```terminal
django-admin startproject setup .
```

é muito comum nós vermos repositorios onde a palavra setup vira o nome do projeto, porem, se analisarmos bem, dentro dessa pasta estão todas as configs do nosso projeto, então e considerado uma boa pratica dar o nome do projeto de setup, o ponto no final do comando serve para não deixar o django criar uma subpasta com o mesmo nome com os arquivos de configs dentro

### 3. Rodando servidor

Após isso, podemos ja ver na tela oque nós estamos fazendo com o seguinte comando

```terminal
python manage.py runserver
```

esse é um dos arquivos e um dos comandos que podemos executar quando criamos nosso projeto usando o ultimo comando, após usarmos esse comando uma mensagem aparece no terminar e um endereço e nos passado, geralmente algo como http://127.0.0.1:8000 aqui podemos clicar nele segurando CRTL e acessar a pagina do projeto que esta rodando em um servidor local

### 4. Variaveis de ambiente e sua importancia 

o que são variaveis de ambiente, bom o proprio nome já diz, são variaveis que iram rodar somente no seu ambiente e nada mais, geralmente são chaves de incriptação, chaves de acesso, senhas ou qualquer dado sensivel que não possa ser visto por todo mundo, essas variaveis nos adiacionamos em um arquivo chamado de .env e para ler ele no python/Django precisamos de uma lib para facilitar nossa vida, então vamos para a instalação

`No seu ambiente virtual digite no terminal o seguinte comando`

```terminal
pip install python-dotenv
```

Após instalarmos o pacote dentro do nosso projeto no arquivo setup/settings.py vamos precisar fazer algumas modificações para isso funcionar, primeiro os imports

```python
#setup/settings.py

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

```

precisaremosm importar a lib os direto do python e tambem o dotenv, após fazermos isso teremos que carregar o dotenv chamando a função load_dotevn()

após isso teremos que remover a nossa SECRET_KEY do arquivo settings.py e por em um arquivo .env atribuindo a uma variavel como no exemplo a seguir

```python
#arquivo .env
SECRET_KEY = sua SECRET_KEY
```

para carregar esse secret key la no arquivo settings.py usaremos o seguinte codigo

```python
#arquivo setup/settings.py

SECRET_KEY = str(os.getenv('SECRET_KEY'))
```

certo, mas mesmo fazendo isso tudo ainda assim o arquivo .env vai ser enviado para nosso github e nossa chave vai ficar exposta, caaaalma meu jovem gafanhoto, é agora que entra magia de tudo, temos um tipo de arquivo chamado .gitignore, esse arquivo e responsavel por mapear todos os arquivos ou pastas que não queremos adicionar a nossa arvore git, ou seja, tudo que tiver descrito neste arquivo o git não irá rastrear e como consequencia não ira adicionar em seus repositorios, e para facilitar ainda mais a nossa vida, tem um site chamado gitignore.io que você bota a linguagem, sistema ou framework que você esta trabalhando e ele gera um gitignore dedicado para oque você esta trabalhando, como nós estamos trabalhando com python/django, só pesquisar django la e colar no seu gitignore oque ele retornar e pronto