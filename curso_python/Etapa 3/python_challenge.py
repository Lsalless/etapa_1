# Desafio
# Crie um programa para uma loja de tintas. O programa deverá pedir o tamanho (em metros quadrados) da área a ser pintada. 
# Considere que a tinta cobre 1 litro para cada 6 metros quadrados e é vendida em latas de 18 litros (custando R$ 80,00) 
# ou em galões de 3,6 litros (custando R$ 25,00).

# O programa deve calcular e exibir as quantidades de tinta necessárias e os respectivos custos em 3 situações:

# . Comprar apenas latas de 18 litros.

# . Comprar apenas galões de 3,6 litros.

# . Misturar latas e galões de forma a minimizar o custo total.

# Além disso, acrescente uma margem de 10% de segurança e sempre arredonde os valores para cima, considerando latas e galões cheios.

import math
#litros com 10% extra
area = float(input("Digite a área em metros quadrados (m²): ").replace(",", "."))
print(f"A área informada foi {area} m²")

litros = area/6*1.1
litros = math.ceil(litros)

#somente latas (18l)
latas = math.ceil(litros/18)
preco_latas=latas*80

#só galões de 3.6l
galoes = math.ceil(litros/3.6)
preco_galoes = galoes *25

#misturar latas e galoes 
latas_misturadas = litros //18
resto = litros %18
galoes_misturados = math.ceil(resto// 3.6)
preco_misturado = (latas_misturadas * 80) + (galoes_misturados *25)

print("\n Só latas de 18L", f"{latas} latas -> R$: {preco_latas:2f}")
print("\n Só galões de 3,6L", f"{galoes} galões -> {preco_galoes:2f}")
print("\n Misturado", f"{latas_misturadas} latas e {galoes_misturados} galões -> R$: {preco_misturado:2f}")



