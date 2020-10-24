def lista_primos(numero):
    lista = [2]

    while numero != 2:

        div = 2
        cont = 0

        while div < numero:
            if numero % div == 0:
                cont += 1
            div += 1

        if cont == 0:
            lista.append(numero)

        numero -= 1
        
    lista.sort()
    return lista