def quantos_uns(numero):
    numero = str(numero)
    soma = 0
    i = 0
    while i < len(numero):
        if numero[i] == "1":
            soma += 1
        i+=1
    return soma