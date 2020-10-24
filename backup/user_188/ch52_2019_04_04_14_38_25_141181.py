def eh_crescente(lista):
    contador = 0
    maximo = lista[0]
    while contador < len(lista):
        if maximo <= lista[contador]:
            maximo = lista[contador]
        else:
            return False
        contador += 1
    return True