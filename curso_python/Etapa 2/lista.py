# Objetivo
# Praticar as operações de Create, Read, Update e Delete (CRUD) utilizando listas, dicionários, conjuntos e tuplas em Python.

# Exercício 1: CRUD em lista
# Crie um programa que permita:

# Adicionar nomes a uma lista
# Exibir todos os nomes
# Atualizar um nome existente
# Remover um nome


nomes = []

def adicionar_nome(nome):
    nomes.append(nome)
    print('Nome adicionado com sucesso!')

def listar_nomes():
    if nomes:
        print('Lista de nomes:')
        for i, nome in enumerate(nomes, 1):
            print(f'{i}. {nome}')
    else:
        print('A lista está vazia.')

def atualizar_nome(indice, novo_nome):
    if 0 <= indice < len(nomes):
        nomes[indice] = novo_nome
        print('Nome atualizado com sucesso!')
    else:
        print('Indice inválido.')

def remover_nome(indice):
    if 0 <= indice < len(nomes):
        removido = nomes.pop(indice)
        print(f'Nome "{removido}" removido com sucesso!')
    else:
        print('Índice inválido.')

print("--- CRUD de Nomes ---")
while True:
    print('\nEscolha uma opção:')
    print('1 - Adicionar nome')
    print('2 - Listar nomes')
    print('3 - Atualizar nome')
    print('4 - Remover nome')
    print('0 - Sair')
    opcao = input('Opção: ')

    if opcao == '1':
        nome = input('Digite o nome para adicionar: ')
        adicionar_nome(nome)
    elif opcao == '2':
        listar_nomes()
    elif opcao == '3':
        listar_nomes()
        if nomes:
            try:
                indice = int(input('Digite o número do nome que deseja atualizar: ')) - 1
                novo_nome = input('Digite o novo nome: ')
                atualizar_nome(indice, novo_nome)
            except ValueError:
                print('Entrada inválida.')
    elif opcao == '4':
        listar_nomes()
        if nomes:
            try:
                indice = int(input('Digite o número do nome que deseja remover: ')) - 1
                remover_nome(indice)
            except ValueError:
                print('Entrada inválida.')
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')




