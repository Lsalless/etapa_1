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


def atualizar_nome(nome_antigo, novo_nome):
    if nome_antigo in nomes:
        idx = nomes.index(nome_antigo)
        nomes[idx] = novo_nome
        print('Nome atualizado com sucesso!')
    else:
        print('Nome não encontrado.')


def remover_nome(nome):
    if nome in nomes:
        nomes.remove(nome)
        print(f'Nome "{nome}" removido com sucesso!')
    else:
        print('Nome não encontrado.')

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
            nome_antigo = input('Digite o nome que deseja atualizar: ')
            novo_nome = input('Digite o novo nome: ')
            atualizar_nome(nome_antigo, novo_nome)
    elif opcao == '4':
        listar_nomes()
        if nomes:
            nome = input('Digite o nome que deseja remover: ')
            remover_nome(nome)
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')




