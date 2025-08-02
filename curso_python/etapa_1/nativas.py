#1- Peça uma palavra ao usuário e mostre quantas letras ela tem com len().

palavra = (input('Me diga uma palavra e eu te direi quantas letras ela tem: '))
total = len(palavra)
print(f'A {palavra} possui {total} palavras.')

# 2- Peça uma lista de 5 números (usando input() e split()) e imprima a soma com sum() e o maior número com max().
numeros = input("Digite 5 números separados por espaço: ").split()

numeros = [int(num) for num in numeros]
soma = sum(numeros)
maior = max(numeros)
print(f"Soma: {soma}")
print(f"Maior número: {maior}")


# 3- Verifique e imprima o tipo de três variáveis diferentes usando type().

def identificar_tipo(valor):
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            if valor.lower() in ['true', 'false']:
                return valor.lower() == 'true'
            return valor  # continua sendo string

entrada1 = input("Digite o primeiro valor: ")
entrada2 = input("Digite o segundo valor: ")
entrada3 = input("Digite o terceiro valor: ")


valor1 = identificar_tipo(entrada1)
valor2 = identificar_tipo(entrada2)
valor3 = identificar_tipo(entrada3)


print("Tipo de valor1:", type(valor1))
print("Tipo de valor2:", type(valor2))
print("Tipo de valor3:", type(valor3))
