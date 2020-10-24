def soma_valores(x):
    valores = []
    for i in range(10):
        x = float(input("Digite um valor: "))
        valores.append(x)
    soma = 0.0
    maior = valores[0]
    for val in valores:
        soma += val
        if val > maior:
            maior = val
    return soma