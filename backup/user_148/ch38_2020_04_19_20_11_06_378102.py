def quantos_uns(n):
    lista = []
    i = 0
    while i<len(n):
        if p[i] == 1:
            lista.append(p[i])
        i += 1
        
    return len(lista)