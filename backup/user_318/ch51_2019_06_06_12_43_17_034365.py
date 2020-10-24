def estritamente_crescente(lista_recebida):
    lista_criada=[]
    i=1
    lista_criada.append(lista_recebida[0])
    while i<len(lista_recebida):
        if lista_recebida[i]>=lista_recebida[i-1]:
            lista_criada.append(lista_recebida[i])
            i+=1
        if lista_recebida[i]<lista_recebida[i-1]:
            del(lista_recebida[i])
            i+=1
    return lista_criada