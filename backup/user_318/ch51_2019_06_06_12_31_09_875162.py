def estritamente_crescente(lista_recebida):
    lista_criada=[]
    i=0
    lista_criada.append(lista_recebida[0])
    while i<len(lista_recebida):
        if lista_recebida[i+1]>=lista_recebida[i]:
            lista_criada.append(lista_recebida[i+1])
            i+=1
        else:
            i+=1
    return lista_criada