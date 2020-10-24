def quantos_uns (numero):
    i = 0
    soma = 0
    while i < len("numero"):
        if numero[i] == "1":
            soma += 1
            i += 1
        else:
            i += 1
    return soma