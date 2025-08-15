from models.restaurantes import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_a_ostra_bebada = Restaurante('a ostra bebada','Bar')
restaurante_bar_do_moe = Restaurante('bar do moe','Bar')
restaurante_sabor_italiano = Restaurante('sabor italiano','Italiano')

bebida_cerveja = Bebida('Cerveja', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')

restaurante_a_ostra_bebada.adicionar_item_no_cardapio(bebida_cerveja)
restaurante_a_ostra_bebada.adicionar_item_no_cardapio(prato_paozinho)


restaurante_a_ostra_bebada.alterar_estado()

bebida_cerveja.aplicar_desconto()
prato_paozinho.aplicar_desconto()


def main():
    #Restaurante.listar_restaurantes()
    restaurante_a_ostra_bebada.listar_cardapio

if __name__ == '__main__':
    main()