# Revendo conceitos básicos de POO em Python

A Programação Orientada a Objetos (POO) é um paradigma que organiza o código em torno de **classes** e **objetos**.  
Vamos revisar alguns conceitos fundamentais aplicados em Python.

---

## 1. Como criar uma classe

Em Python, criamos uma classe usando a palavra-chave `class`.  
O método especial `__init__` é o **construtor**, chamado quando o objeto é criado.

```python
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

## 2. Como criar uma classe

Instanciar uma classe significa criar um objeto a partir dela.
Basta chamar o nome da classe como se fosse uma função, passando os parâmetros esperados pelo __init__.

```python
cliente1 = Cliente("maria", 30)
cliente2 = Cliente("João", 25)

print(cliente1.nome) # Maria
print(cliente2.idade) # 25
```

## 3. Qual a importância de um parâmetro privado (self._cliente)
Em Python, por convenção, um atributo iniciado com underscore (_) é considerado protegido (uso interno).
Isso indica que ele não deve ser acessado diretamente fora da classe, evitando alterações indevidas e mantendo o encapsulamento.

```python
class ContaBancaria:
    def __init__(self, cliente, saldo):
        self._cliente = cliente  # atributo protegido
        self.saldo = saldo

conta = ContaBancaria("Maria", 1000)
print(conta._cliente)  # Possível, mas não recomendado
```

## 4. Quando e como usar @property
O decorador @property permite transformar um método em um atributo de leitura, mantendo o acesso simples e protegido.
É útil quando queremos controlar como um valor é obtido, sem mudar a forma como ele é acessado.

### IMPORTANTE: QUANDO FOREM CHAMAR UMA PROPERTY NÃO USEM PARENTESES EM SUA CHAMADA EX: produtp_ex.preco 

```python
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def preco(self):
        return f"R$ {self._preco:.2f}"

p = Produto("Notebook", 3500)
print(p.preco)  # R$ 3500.00
```
Use @property quando precisar proteger atributos, formatar valores ou executar lógica extra na leitura.

## 5. Quando e como usar @classmethod
O @classmethod é usado quando queremos criar métodos que recebem a classe (cls) como primeiro parâmetro,
em vez de receber a instância (self).
Ele é útil para métodos de fábrica (que criam objetos de forma alternativa) ou para acessar/modificar atributos da classe.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_anonimo(cls):
        return cls("Anônimo", 0)

p1 = Pessoa.criar_anonimo()
print(p1.nome)  # Anônimo

```

## 6. Quando e como usar Heranças
As heranças sempre serão nossas aliadas quando o assunto é padronização de codigo e reaproveitamento do mesmo, fazendo classes filhas herdarem parâmetros da classe pai, assim se criarmos 6 classes que usam os parametros "preco" e "nome" podemos criar uma classe pai que passara esses parametros para a classe filha via herança

```python
#Classe Prato herdando parametros da classe ItemCardapia por meio do objeto especial "super()" usando o inicializador da classe pai e passando como parametro os itens herdados 

#IMPORTANTE: Para usar Herança tem que se passar a Classe pai como parametro para Classe filha class Prato(ItemCardapio):
from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__ (self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

```
## 7. Classes abstratas e Polimorfismo

Classe abstrata → é um modelo que não pode ser instanciado diretamente, usado para definir métodos obrigatórios que as subclasses devem implementar. Em Python, usamos from abc import ABC, abstractmethod.

Polimorfismo → é a capacidade de diferentes classes responderem de formas diferentes ao mesmo método, permitindo código mais flexível e genérico

### A classe abstrata é implementada na classe pai que as outras irão herdar 
```python

from abc import ABC, abstractmethod

class ItemCardapio:

    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    #implementando classe abstrata na classe pai
    @abstractmethod
    def aplicar_desconto(self):
        pass

```
em seguida conseguimos implementar essa classe abstrata na classe filha do jeito que queremos, assim podemos assegurar que uma classe ou metodo sempre sera usado, nem que seja com um simples pass ou com logicas complexas a nossa vontade

```python

from models.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho):

        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome

    #methodo com a classe abstrata usando o conceito de polimorfismo 
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)

```

## 8. Dependencias e ambientes virtualizados

#### Porque usar um ambiente virtual?
as vezes quando estamos trabalhando em um time com varias maquinas diferentes, ficar instalando dependencias sem um ambiente virtualizado se torna um trabalho exaustivo, pois alem de lotar o seu computador com bibliotecas e frameworks, para que seu projeto funcione em outra maquina, o prejeto precisa ter exatamente as mesma bibliotecas e frameworks nas mesmas versoes que estamos usando em nossas maquinas, é ai que o ambiente virtual entra em cena, o ambiente virtual "cria um computador dentro do seu computador" e como se o python estivesse rodando em um computador a parte, instalando as dependencias referentes aquele projeto dentro daquele computador virtual dentro da sua maquina, isso garante que as tudo que precise ser instalado nao instale em seu computador, e que o projeto rode com as exatas dependencias que ele necessita, vamos ver como que nós criamos, instalamos e iniciamos um ambiente virtualizado a seguir, para este exemplo usaremos o [VENV](https://docs.python.org/3/library/venv.html) do proprio Python

para criar o ambiente virtual, na raiz do seu projeto digite isso no terminal:

`python -m venv venv`

#### OBS: o segundo 'venv' no comando e usado para nomear o ambiente virtual, mas por convenção deixamos ele como venv mesmo

logo quando executar o comando vera que na raiz do seu porjeto uma pasta sera criada com subpastas dentro, abordaremos oque é cada uma mais para frente mas logo de cara as que você tem que saber oque significa são 

* Lib
    * Aqui nessa pasta sera guardada toda e qualquer dependencias e pacotes que instalarmos no nosso projeto
* Scripts
    * Aqui serão armazenados todos os scripts referentes aquele ambiente virtual, inclusive o proprio script de ativação e desativação do ambiente virtual se encontra aqui dentro

em suma de introdução é oque podemos saber, conforme for passando podemos nos aprofundar mais e vamos nos aprofundar mais em relação a ambientes virtualizados

e para ativar ele como fazermos, porque só criar o ambiente sem ativa-lo é a mesma coisa que estavamos fazendo antes, instalar e executar as coisas na nossa própria maquina

para ativar o nosso ambiente virtual e bem facil, novamente na raiz do nosso projeto, vá até o terminal e digite

`.\venv\Scripts\activate.ps1`

### IMPORTANTE: se entrarem na pasta venv dentro da pasta Scripts verão que tem varios arquivos de Activate, a ativação do venv pode ser diferente do meu computador para o seu, e esses scripts nomeados Activate são os scripts que inicializão nosso ambiente virtual, o comando que escrevemos acima só faz executar esse script então se um deles não deu certo tente o outro, o comando muda de mac/linux para windows

caso de certo e você ative seu ambiente virtual, no seu terminal antes do caminho do seu computador tera um **(venv)** escrito conforme o exemplo abaixo

`(venv) PS C:\Users\guilherme\OneDrive\Documentos\Estudos\estudos\Python\python-aplicando-orientacao-objetos> `

para desativar o ambiente virtual basta digitar a palavra **deactivate** no terminal e pronto o ambiente sera "desmontado" 

`deactivate`

Voce sabe que saiu do ambiente virtual quando o **(venv)** nao aparece mais a frente do caminho do diretorio no terminal

para instalar dependencias e pacotes no ambiente virtual para esse exemplo estarei usando o **pip** que para instalar os pacotes e libs e muito simples basta escrever no seu terminarl pip install e o nome do pacote como no exemplo a seguir

`pip install requests`

o pip nao e nada mais nada a menos que o npm do javascript, ele é um gerenciador de pacotes para o python, para saber se o seu pacote foi instalado com sucesso execute o comando **pip freeze**, esse comando ele retorna todas os pacotes que instalamos no nosso ambiente 

```
pip freeze

certifi==2025.8.3
charset-normalizer==3.4.3
idna==3.10
requests==2.32.4
urllib3==2.5.0

```

e como conseguimos garantir que nossos colegas vão conseguir instalar esses mesmos pacotes que nos temos instalados na nossa maquina, simples usando o mesmo comando do pip freeze com um temperinho a mais 

```
pip freeze > requirements.txt
```

aqui nos informamos que nos queremos que crie um arquivo chamado requirements.txt com tudo que o comando pip freeze retorna, assim asseguramos que toda vez que instalarmos um pacote novo no projeto, ao executarmos esse comando, o arquivo e atualizado com as dependencias que nos temos no projeto, assim quem pegar o nosso projeto e so executar o comando **pip install -r requirements.txt** assim o comando do pip vai passar linha por linha do nosso arquivo requirements.txt instalando os pacotes que estao descritos lá, de maneira bem resumida é isso

