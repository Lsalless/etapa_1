# 1 -  Peça ao usuário que digite seu nome e exiba uma mensagem de boas-vindas com o nome.

nome = input( 'Olá, me diga o seu nome?: ')
print(f'Olá {nome} seja bem vindo!')

# 2 - Solicite dois números e exiba a soma deles.

a = int(input('Me dê um valor: '))
b = int(input('Me dê outro valor: '))

total = a+b
print(f' A soma dos dois valores é = {total}')

# 3 - Receba a idade do usuário e exiba quantos anos ele terá em 10 anos.

presente = int(input('Me diga a sua idade?'))
print(f'Daqui a 10 anos, você terá {presente+10}')