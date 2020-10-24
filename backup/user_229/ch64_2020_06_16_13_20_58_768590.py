def acha_bigramas(string):
    lista = []
    for i in range(len(string) - 1):
        if '{0}{1}'.format(string[i], string[i+1]) not in lista:
            lista.append('{0}{1}'.format(string[i], string[i+1]))
                     
    return lista