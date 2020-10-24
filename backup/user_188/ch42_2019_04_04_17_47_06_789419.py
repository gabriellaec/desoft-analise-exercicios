def quantos_uns(numero):
    contador = 0
    num_uns = 0
    str(numero)
    while contador < len(numero):
        if numero[contador] == "1":
            num_uns += 1
        contador += 1
    return num_uns