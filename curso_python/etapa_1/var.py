# 1 - Armazene seu nome, idade e cidade em três variáveis diferentes e imprima uma frase usando esses dados.
nome='Laíssa'
idade= 26
cidade= 'Niterói'
print(f'A {nome} tem {idade} e mora na cidade de {cidade}')

# 2 -  Troque os valores de duas variáveis entre si (ex: a = 10, b = 20 → a = 20, b = 10).
a = 10
b = 5
print(f'Antes da troca: a = {a}, b = {b}')

a, b = b, a 

print(f'depois a troca: a = {a}, b = {b}')

#3 - Crie uma variável com o valor 100, depois aumente esse valor em 25 e imprima o novo resultado.

valor = 100
print(f'O valor antes da alteração é: {valor}')

valor = 125 
print(f'O valor após a alteração é: {valor}')
