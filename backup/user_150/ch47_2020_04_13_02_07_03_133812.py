def estritamente_crescente(lista):
    if len(lista) == 0:
        return lista
    else:
        inicial = lista[0]
        lista_crescente = [inicial]
        for numero in lista:
            if numero > lista[0]:
                lista_crescente.append(numero)
        return lista_crescente