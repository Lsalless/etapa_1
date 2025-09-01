# Neste exercicio queremos uma calculadora com as quatro funções básicas, porem devemos trabalhar com suas funcões em coleções.

# somar, substração, multiplicação, divisão.


def entrada():
    return input('Qual operação você deseja utilizar? (soma, subtracao, multiplicacao, divisao): ')


def somar(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


total = 0
prosseguir = 'sim'

while prosseguir == 'sim':
    operacao = entrada()
    num1 = float(input(f'Diga o primeiro número da operação {operacao}: '))
    num2 = float(input(f'Diga o segundo número da operação {operacao}: '))

    if operacao == "soma":
        resultado = somar(num1, num2)
    elif operacao == "subtracao":
        resultado = subtracao(num1, num2)
    elif operacao == "multiplicacao":
        resultado = multiplicacao(num1, num2)
    elif operacao == "divisao":
        resultado = divisao(num1, num2)
    else:
        print("Operação inválida.")
        continue

    print(f"Seu resultado é: {resultado}")
    total += resultado
    prosseguir = input("Deseja continuar? (sim/não): ")

print(f"Total acumulado: {total}")
    


