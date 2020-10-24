def numero_no_indice(liste):
    lista=[]
    i=0
    while i < len(liste):
        if  liste[i]==i:
            lista.append(liste[i])
        i+=1
    return lista