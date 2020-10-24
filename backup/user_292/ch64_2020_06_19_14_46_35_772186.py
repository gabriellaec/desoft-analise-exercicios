def acha_bigramas(palavra):
    lista = []
    lista_v=[]
    for i in range(len(palavra)):
        if i+2 <= len(palavra):
            lista.append(palavra[i:i+2])
    for n in lista:
        if n not in lista_v:
            lista_v.append(n)
    return lista_v