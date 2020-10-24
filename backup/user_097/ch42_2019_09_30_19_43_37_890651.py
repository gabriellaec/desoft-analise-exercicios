def quantos_uns(numero):
    numero = str(numero)
    contador = 0
    for i in numero:
        if (i=="1"):
            contador = contador + 1
    return contador

print(quantos_uns(111987111))