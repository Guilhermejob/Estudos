import os

restaurantes = [
    {'nome':'Bar do Moe', 'categoria':'Bar', 'ativo':True}, 
    {'nome':'A Ostra Bebada', 'categoria':'Bar', 'ativo':True},
    {'nome':'Sabor Italiano', 'categoria':'Restaurante', 'ativo':False}
]

def exibir_nome_do_programa():

    print("""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Auterar estado do restaurante')
    print('4. Sair \n')

def finalizar_app():
    exibir_sub_titulo('Finalizando Programa\n')

def opção_invalida():
    print('Opção inválida!')

    voltar_ao_menu_principal()
 
def cadastrar_novo_restaurante():
    exibir_sub_titulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'\nDigite a categoria de {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu_principal()

def listar_restaurantes():

    exibir_sub_titulo('Lista de restaurantes Cadastrados: \n')

    for restaurante in restaurantes:
        print(f'nome: {restaurante['nome']} - Categoria: {restaurante['categoria']} - {'Ativado' if restaurante['ativo'] else 'Desativado'}')

    voltar_ao_menu_principal()

def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                auterar_estado_do_restaurante()
            case 4:
                finalizar_app()
            case _:
                finalizar_app()
                print('Opção inválida!')

    except:
        opção_invalida()

def voltar_ao_menu_principal():
    input('\ndigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_sub_titulo(texto):
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(f'{texto}')
    print(linha)

def auterar_estado_do_restaurante():
    exibir_sub_titulo('Auterar estado do restaurante: \n')

    nome_restaurante = input('Digite o nome do restaurante: \n')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'

            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()
     

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()