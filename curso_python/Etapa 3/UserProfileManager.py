# Implemente criar_perfil(**kwargs) que recebe dados como nome, idade, email, e retorna um dicionário com essas informações. 
# Não se limite apenas as sugestões, esse treino é importante para o futuro

def criar_perfil(**kwargs):
    return dict(kwargs)

dados = {}
while True:
    chave = input("Digite o nome do campo (ex: nome, idade, email) ou 'sair' para finalizar: ")
    if chave.lower() == 'sair':
        break
    valor = input(f"Digite o valor para '{chave}': ")
    dados[chave] = valor

perfil = criar_perfil(**dados)
print(perfil)