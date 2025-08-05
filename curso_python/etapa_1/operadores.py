# -  Operadores matemáticos e lógicos
#1 -  Peça dois números e exiba o resultado das quatro operações básicas entre eles.

n1 = int(input('Me diga um número?: '))
n2 = int(input('Agora me diga outro número?: '))
print(f' A soma é = {n1+n2}, a subtração é = {n1-n2}, a multiplicação é = {n1*n2}, a divisão é = {n1/n2}')

#2 -  Verifique se um número informado pelo usuário é par ou ímpar.

import math

num = int(input('Digite um número: '))
num_arredondado = math.floor(num)

if num_arredondado % 2 == 0:
  print(f'O {num} é par!')
else:
  print(f'o {num} é ímpar!')


#3 - Solicite a idade de uma pessoa e verifique se ela tem entre 18 e 30 anos e se tem carteira de motorista (pergunte com input se sim ou não).

idade = int(input('E qual é a sua idade?: '))
verificacao = 18 >= idade <=30
print(f'Verificando a sua idade: {verificacao}')
cnh = input(f'Você tem carteira de motorista? (sim/não): ').strip().lower()
