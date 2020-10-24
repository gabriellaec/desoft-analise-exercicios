def classifica_lista (lista):
    c=0
    u=0
    i=0
    if len(lista) < 2:
        return 'nenhum'
    else:
        while i< (len(lista)-1):
            if lista[i] > lista[i-0]:
                c+=1
                i+=1
            if lista[i] < lista[i-0]:
                u+=1
                i+=1
        if c == len(lista):
            return 'crescente'
        if u == len(lista):
            return 'decrescente'
        else:
            return 'nenhuma'