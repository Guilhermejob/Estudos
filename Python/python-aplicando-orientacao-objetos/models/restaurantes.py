from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Ativo: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Ativo'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):

        nota_final = nota

        if nota_final > 5:
            nota_final = 5

        if  0 < nota_final <= 5:
            avaliacao = Avaliacao(cliente, nota_final)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        try:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_de_notas = len(self._avaliacao)
            media = round(soma_das_notas / quantidade_de_notas, 1)
            return media
        except:
            return 'Sem Avaliações'

    def adicionar_item_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)


    @property
    def listar_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        #tamanho = prato._tamanho if prato._tamanho else ''
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)


            
  
        
