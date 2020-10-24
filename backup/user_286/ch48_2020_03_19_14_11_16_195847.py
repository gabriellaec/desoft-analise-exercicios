def estritamente_crescente (lista):
    lista_final = [lista[0]]
    for numero in lista:
        if lista_final[-1] < lista[lista.index(numero)]:
            lista_final.append(numero)

    return lista_final

def eh_crescente(lista):
    if estritamente_crescente(lista) == lista:
        return True
    else:
        return False
