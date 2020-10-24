def estritamente_crescente(lista):
    i=0
    resp=[]
    while i < len(lista):
        if lista[i] > lista[i-1]:
            resp.append(lista[i])
        i+=1
    return resp