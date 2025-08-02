# 1 - Imprima os números de 1 a 10 usando for.

for i in range(1, 11):
  print(i)


# 2 -  Peça um número e exiba a tabuada dele de 1 a 10 usando while.
tabuada = int(input("Me diga qual tabuada você gostaria de saber: "))
i = 1
while i<=10:
  print(f"{tabuada} x {i} = {tabuada*i}")
  i+=1

#3-  Crie uma lista com 5 nomes e use for para imprimir um por linha.

nomes=['Laíssa', 'Gustavo', 'Luiz', 'Rozi', 'Giovanna']

for nome in nomes:
    print(f"{nome}\n")
