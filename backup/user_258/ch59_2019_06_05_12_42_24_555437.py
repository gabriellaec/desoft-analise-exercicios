def conta_a(string):
    lista_a = []
    lista_string = list(string)
    for k in lista_string:
        if k == 'a':
            lista_a.append(k)
    return len(lista_a)