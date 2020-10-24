def numero_no_indice(lista):
    i=0
    resp=[]
    while i < len(lista):
        if lista[i] == i:
            resp.append(i)
        i +=1
    return resp