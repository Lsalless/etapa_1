# Exercício 2: CRUD em dicionário
# Crie um dicionário de contatos com nome e telefone:

# Adicionar um contato
# Buscar um contato
# Atualizar o telefone
# Remover um contato`
# ----------------

contato = {}


def adicionar_contato(nome, numero):
    contato[nome] = numero
    print('Contato adicionado com sucesso!')


def buscar_contato():
    if contato:
        print('Lista de contatos:')
        for nome, telefone in contato.items():
            print(f'Nome: {nome} | Telefone: {telefone}')
    else:
        print('Nenhum contato cadastrado.')
    

def remover_contato(nome):
    if nome in contato:
        del contato[nome]
        print(f'Contato "{nome}" removido com sucesso!')
    else:
        print('Contato não encontrado.')
continuar = 'Sim'


print("--- CRUD de Contatos ---")
while True:
    print('\nEscolha uma opção:')
    print('1 - Adicionar contato')
    print('2 - Listar contatos')
    print('3 - Remover contato')
    print('0 - Sair')
    opcao = input('Opção: ')

    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        numero = input('Digite o telefone do contato: ')
        adicionar_contato(nome, numero)
    elif opcao == '2':
        buscar_contato()
    elif opcao == '3':
        nome = input('Digite o nome do contato que deseja remover: ')
        remover_contato(nome)
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')


