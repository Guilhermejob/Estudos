## 1. Dependencias e ambientes virtualizados

#### Porque usar um ambiente virtual?
as vezes quando estamos trabalhando em um time com varias maquinas diferentes, ficar instalando dependencias sem um ambiente virtualizado se torna um trabalho exaustivo, pois alem de lotar o seu computador com bibliotecas e frameworks, para que seu projeto funcione em outra maquina, o prejeto precisa ter exatamente as mesma bibliotecas e frameworks nas mesmas versoes que estamos usando em nossas maquinas, é ai que o ambiente virtual entra em cena, o ambiente virtual "cria um computador dentro do seu computador" e como se o python estivesse rodando em um computador a parte, instalando as dependencias referentes aquele projeto dentro daquele computador virtual dentro da sua maquina, isso garante que as tudo que precise ser instalado nao instale em seu computador, e que o projeto rode com as exatas dependencias que ele necessita, vamos ver como que nós criamos, instalamos e iniciamos um ambiente virtualizado a seguir, para este exemplo usaremos o [VENV](https://docs.python.org/3/library/venv.html) do proprio Python

para criar o ambiente virtual, na raiz do seu projeto digite isso no terminal:

```terminal
python -m venv venv
```

#### OBS: o segundo 'venv' no comando e usado para nomear o ambiente virtual, mas por convenção deixamos ele como venv mesmo

logo quando executar o comando vera que na raiz do seu porjeto uma pasta sera criada com subpastas dentro, abordaremos oque é cada uma mais para frente mas logo de cara as que você tem que saber oque significa são 

* Lib
    * Aqui nessa pasta sera guardada toda e qualquer dependencias e pacotes que instalarmos no nosso projeto
* Scripts
    * Aqui serão armazenados todos os scripts referentes aquele ambiente virtual, inclusive o proprio script de ativação e desativação do ambiente virtual se encontra aqui dentro

em suma de introdução é oque podemos saber, conforme for passando podemos nos aprofundar mais e vamos nos aprofundar mais em relação a ambientes virtualizados

e para ativar ele como fazermos, porque só criar o ambiente sem ativa-lo é a mesma coisa que estavamos fazendo antes, instalar e executar as coisas na nossa própria maquina

para ativar o nosso ambiente virtual e bem facil, novamente na raiz do nosso projeto, vá até o terminal e digite

```terminal
.\venv\Scripts\activate.ps1
```

### IMPORTANTE: se entrarem na pasta venv dentro da pasta Scripts verão que tem varios arquivos de Activate, a ativação do venv pode ser diferente do meu computador para o seu, e esses scripts nomeados Activate são os scripts que inicializão nosso ambiente virtual, o comando que escrevemos acima só faz executar esse script então se um deles não deu certo tente o outro, o comando muda de mac/linux para windows

caso de certo e você ative seu ambiente virtual, no seu terminal antes do caminho do seu computador tera um **(venv)** escrito conforme o exemplo abaixo

```terminal
(venv) PS C:\Users\guilherme\OneDrive\Documentos\Estudos\estudos\Python\python-aplicando-orientacao-objetos> 
```

para desativar o ambiente virtual basta digitar a palavra **deactivate** no terminal e pronto o ambiente sera "desmontado" 

```terminal
deactivate
```

Voce sabe que saiu do ambiente virtual quando o **(venv)** nao aparece mais a frente do caminho do diretorio no terminal

para instalar dependencias e pacotes no ambiente virtual para esse exemplo estarei usando o **pip** que para instalar os pacotes e libs e muito simples basta escrever no seu terminarl pip install e o nome do pacote como no exemplo a seguir

```terminal
pip install requests
```


o pip nao e nada mais nada a menos que o npm do javascript, ele é um gerenciador de pacotes para o python, para saber se o seu pacote foi instalado com sucesso execute o comando **pip freeze**, esse comando ele retorna todas os pacotes que instalamos no nosso ambiente 

``` terminal
pip freeze

certifi==2025.8.3
charset-normalizer==3.4.3
idna==3.10
requests==2.32.4
urllib3==2.5.0

```

e como conseguimos garantir que nossos colegas vão conseguir instalar esses mesmos pacotes que nos temos instalados na nossa maquina, simples usando o mesmo comando do pip freeze com um temperinho a mais 

```terminal
pip freeze > requirements.txt
```

aqui nos informamos que nos queremos que crie um arquivo chamado requirements.txt com tudo que o comando pip freeze retorna, assim asseguramos que toda vez que instalarmos um pacote novo no projeto, ao executarmos esse comando, o arquivo e atualizado com as dependencias que nos temos no projeto, assim quem pegar o nosso projeto e so executar o comando **pip install -r requirements.txt** assim o comando do pip vai passar linha por linha do nosso arquivo requirements.txt instalando os pacotes que estao descritos lá, de maneira bem resumida é isso

## 2. Requests HTTP
O HTTP é basicamente o jeito que seu computador conversa com outros computadores na internet — tipo mandar e receber cartas, só que rapidinho e em bits.

Quando a gente usa Python, a biblioteca requests é tipo um carteiro super eficiente que entrega e busca essas cartas pra você sem frescura.

Por exemplo:

```python
import requests

# Mandando uma "carta" (requisição GET)
resposta = requests.get("https://api.github.com")
print(resposta.status_code)  # 200 significa "tudo certo"
print(resposta.json())       # já devolve o conteúdo em formato de dicionário
```

O .get() é pra pedir dados, o .post() é pra enviar coisas (tipo formulários ou JSON), e ainda tem .put(), .delete(), etc.

Você também pode mandar headers, params e até autenticação junto, caso o "destinatário" precise saber quem você é ou o que exatamente você quer.

O bom do requests é que ele já faz muita coisa chata por baixo dos panos, como lidar com encoding, cookies e redirecionamentos, então você só foca no que precisa pegar ou enviar, e manipular esses dados como sua demanda necessitar.

## 2. Criando nosso primeiro endpoint e usando o FastAPI

Aqui nos começaremos a entrar em um terreno para construir um backand que faz interações com uma API externa, mas oque é a API?
``Uma API é tipo um "garçom" entre dois programas: você faz o pedido (requisição), ela leva pra cozinha (o servidor) e te traz a resposta pronta.``
em termos mais leigos seria isso.

primeiro instalaremos a o FastAPI, e como se fosse um micro Framework que vai nos ajudar com a parte de requisições HTTP, e se você esta lendo isso ja sabe como se instala um pacote, mas vou por aqui para relembrarmos

```terminal
pip install fastapi
```

mas calma, sempre antes de instalarmos um pacote ou um framework no nosso projeto `SEMPRE LEIAM A DEOCUMENTAÇÃO DO QUE VOCÊ ESTA INSTALANDO`, eu como sei disso li a documentação do fastapi, é so pesquisar no google e ir no site oficial deles e la pede para instalarmos mais um pacote em nosso projeto que é o Uvicorn, então vamos a instalação dele 

```terminal
pip install uvicorn
```

esse uvicorn vai ser responsavel por criar um servidor para nossa aplicação, e agora que instalamos coisas novas no nosso projeto, vamos atualizar nosso requirements.txt

```terminal
pip freeze > requirements.txt
```

depois que vocês fizerem os codigos e as rotas de vocês para iniciarmos nosso servidor local usaremos o seguinte comando:
```terminal
uvicorn main:app --reload
```



