def remove_vogais(string):
    lista_v = ['a','e','i','o','u']
    lista2 = []
    for i in string.lower():
        if i not in lista_v:
            lista2.append(i)
    return ''.join(lista2)