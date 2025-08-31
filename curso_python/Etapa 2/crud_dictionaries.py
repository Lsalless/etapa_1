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

def atualizar_telefone(nome, novo_numero):
    if nome in contato:
        contato[nome] = novo_numero
        print('Telefone atualizado com sucesso!')
    else:
        print('Contato não encontrado.')



def listar_contatos():
    if contato:
        print('Lista de contatos:')
        for nome, telefone in contato.items():
            print(f'Nome: {nome} | Telefone: {telefone}')
    else:
        print('Nenhum contato cadastrado.')

def buscar_contato_por_nome(nome):
    if nome in contato:
        print(f'Nome: {nome} | Telefone: {contato[nome]}')
    else:
        print('Contato não encontrado.')
    

def remover_contato(nome):
    if nome in contato:
        del contato[nome]
        print(f'Contato "{nome}" removido com sucesso!')
    else:
        print('Contato não encontrado.')



seguir = "sim"
print("Lista de Contatos")
while seguir == "sim":
    print("Digite 1 para Adicionar ou Alterar um contato.\nDigite 2 para Listar os contatos.\nDigite 3 para Remover um contato")
    acao = input()
    
    if acao == "1":
        nome_adicionar = input("Qual nome você deseja adicionar ou alterar o telefone? ")
        telefone_adicionar = input("Qual o telefone que você deseja adicionar ou alterar? ")

        atualizar_telefone(nome_adicionar, telefone_adicionar)

    elif acao == "2":
        listar_contatos()
    
    elif acao == "3":
        nome_remover = input("Qual contato você deseja remover?")
        remover_contato(nome_remover)

    else:
        print("Resposta inválida, selecione uma opção correta.")
        
    continuar = input("Você deseja seguir? ")