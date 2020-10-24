def classifica_lista(l):
    if len(l) <= 2:
        return "nenhum"
    lista = []
    for e in range(1, len(l)):
        if l[e] > l[e-1]:
            lista.append(1)
        elif l[e] < l[e-1]:
            lista.append(-1)
    
    if 1 in lista and -1 in lista:
        return "nenhum"
    elif 1 in lista:
        return "crescente"
    else:
        return "decrescente"