

def stats(*args):
    try:
        if not args:
            return None
        args = [float(x) for x in args]
        minimo = min(args)
        maximo = max(args)
        media = sum(args) / len(args)
        return (minimo, maximo, media)
    except ValueError:
        return "Por favor, digite apenas números válidos."



while True:
    entrada = input("Digite os números separados por espaço: ")
    numeros = entrada.split()
    if numeros:
        resultado = stats(*numeros)
        print(resultado)
    else:
        print("Nenhum número informado.")
    continuar = input("Deseja calcular novamente? (sim/não): ")
    if continuar.strip().lower() in ["nao", "não", "n", "no"]:
        break