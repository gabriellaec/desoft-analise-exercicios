def acha_bigramas(palavra):
    lista = []
    for i in range(len(palavra)-1):
        n = palavra[i] + palavra[i+1]
        if n not in lista:
            lista.append(n)   
    return lista
        