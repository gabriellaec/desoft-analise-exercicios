def numero_no_indice(lista):
    i=0
    lista1=[]
    while i<len(lista):
        if lista[i]=="i":
            lista1.append("i")
        i+=1
        return lista[i]