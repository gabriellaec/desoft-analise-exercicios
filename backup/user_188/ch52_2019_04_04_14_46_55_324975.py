def eh_crescente(lista):
    contador = 1
    maximo = lista[0]
    while contador < len(lista)-1:
        if maximo < lista[contador]:
            maximo = lista[contador]
        else:
            return False
        contador += 1
    return True