def quantos_uns (numero):
    i = 0
    contador = 0
    while (i < len(numero)):
        if (numero[0] == 1):
            contador += 1
        i += 1

numero = int(1010102029201)

print (quantos_uns(numero))
