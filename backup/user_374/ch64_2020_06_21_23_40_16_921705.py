'''def acha_bigramas(string):
    lista = []
    lista2 = []
    
    for i in range(0,len(string)):
        lista.append(string[i:i+2])
        
    for i in lista:
        if len(i) >= 2:
            if i not in lista2:
                lista2.append(i)
    return lista2'''

def acha_bigramas(string):
    lista_bigramas = []
    segunda_lista = []

    for intervalo in range(0,len(string)):
        if string[intervalo:intervalo+2] not in lista_bigramas:
            lista_bigramas.append(string[intervalo:intervalo+2])

    for i in lista_bigramas:
        if len(i) == 2:
            segunda_lista.append(i)

    return segunda_lista
