#Input
#input é uma função que permite que o usuario envie uma informação para o python através do terminal

#EX 1:. 
# nome_do_pet = input('Digite o nome do seu pet: ')

# print(f'O nome do pet é: {nome_do_pet}')


#EX 2:.
# idade = int(input('Digite a sua idade: '))
# altura = float(input('Digite sua altura: '))

# print(f'Sua idade é {idade} e sua altura é {altura} m')

def main():
    nomes_pets = []
    while True:
        print('1. Salvar o nome do pet')
        print('2. Parar execução do programa')
        opcao = int(input('Oque deseja Fazer?'))
        
        if opcao == 1:
            nome = input('Digite o nome do pet: ')
            nomes_pets.append(nome)
            print (f'Lista atual de pets: {nomes_pets}')
        if opcao == 2:
            break


if __name__ == '__main__':
    main()