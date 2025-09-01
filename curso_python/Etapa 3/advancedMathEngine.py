# A mesma calculadora agora deve poder fazer operaçoes de raiz e potencia, porém devemos passar qual fator será usado Exemplo: 
# (fator, numero) = 4³ Dica: numero ** fator (exponencial) numero ** (1/fator) (raiz)
# Neste exercicio queremos uma calculadora com as quatro funções básicas, porem devemos trabalhar com suas funcões em coleções.

# somar, substração, multiplicação, divisão.


def entrada():
    return input('Qual operação você deseja utilizar? (soma, subtracao, multiplicacao, divisao, potencia ou raiz): ')


def somar(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b

def potencia(a, b):
    return a ** b 

def raiz(a, b):
    return  a ** (1/b)
    


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

    elif operacao == "potencia":
        resultado = potencia(num1, num2)

    elif operacao == "raiz":
        resultado = raiz(num1, num2)

    else:
        print("Operação inválida.")
        continue

    print(f"Seu resultado é: {resultado}")
    total += resultado
    prosseguir = input("Deseja continuar? (sim/não): ")

print(f"Total acumulado: {total}")
    


