# Exercício 4: Criar e acessar tupla
# Crie uma tupla com 3 cores
# Acesse a segunda cor
# Tente alterar a cor (e veja o que acontece). Coloque o resultado como comentario'

cores = ('azul', ' rosa', 'vermelho')
print(f'nós temos como segunda cor a {1}')
cores [1] = 'amarelo'

#TypeError: 'tuple' object does not support item assignment
#As tuplas não permitem alterações, são imutaveis.
