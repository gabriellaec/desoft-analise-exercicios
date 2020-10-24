def numero_no_indice(lista):
    num=len(lista)
    nova=[]
    i=0
    while i<num:
        if i==lista[i]:
            nova.append(lista[i])
        i+=1
    return nova