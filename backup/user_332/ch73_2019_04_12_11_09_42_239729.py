def remove_vogais (p):
    lista = ['a','e','i','o','u']
    lista2 = []
    word = 0
    for element in p:
        if not element in lista:
            lista2.append(element)
            
    return (''.join(lista2))


