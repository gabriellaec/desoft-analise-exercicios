def eh_crescente(lista):
    maximo = lista[0]
    contador = 1
    while contador < len(lista):
        if maximo >= lista[contador]:
            return False
        contador += 1
    return True