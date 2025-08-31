# Exercício 3: Criar e manipular um set
# Crie um conjunto com 3 nomes de linguagens de programação
# Adicione uma nova linguagem
# Remova uma linguagem
# Verifique se "Python" está no conjunto


linguagens ={'python', 'java', 'ruby'}
print(linguagens)
linguagens.add('php')
linguagens.remove('ruby')

if 'python' in linguagens:
    print('Sim, tem python aqui')
else:
    print('Não temos python aqui')

