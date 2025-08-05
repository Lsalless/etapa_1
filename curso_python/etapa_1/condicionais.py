# 1- Peça um número e diga se ele é positivo, negativo ou zero.

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


# 3 - Peça a idade e informe se a pessoa é criança (até 12), adolescente (13–17), adulto (18–59) ou idoso (60+).

idade = int(input('Me diga a sua idade?: '))

if idade <= 12:
    print('Você é uma criança')

elif idade <= 17:
    print('Você é um adolescente')

elif idade <= 59:
    print('Olá, adulto')

else:
    print('Oi senhor')


#2- Solicite a nota de um aluno e diga se ele foi aprovado (nota ≥ 7), em recuperação (nota entre 5 e 6.9) ou reprovado (abaixo de 5).

aluno = float(input('Me diga a sua nota: '))

if aluno >= 7:
    print('Você foi aprovado')
elif  5 <= aluno:
    print('você está de recuperação')
else:
    print('você está reprovado')