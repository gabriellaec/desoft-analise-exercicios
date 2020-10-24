def numero_no_indice(l):
    lista_resposta=[]
    i=0
    
    while i<len(l):
        if l[i]==i:
            lista_resposta.append(l[i])
        i+=1
    return lista_resposta