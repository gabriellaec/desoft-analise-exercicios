def numero_no_indice(lista):
    num=len(lista)
    nova=[]
    for i in range(0,num):
        if i==lista[i]:
            nova.append(lista[i])
        i+=1
    return nova