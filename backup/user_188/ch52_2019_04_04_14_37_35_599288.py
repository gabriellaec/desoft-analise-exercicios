def eh_crescente(lista):
    contador = 0
    maximo = lista[0]
    while contador < len(lista):
        if maximo <= lista[contador]:
            return False
    return True