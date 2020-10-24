def numero_no_indice(lista):
    produto=[]
    i=0
    while(i<len(lista)):
        if(i==lista[i]):
            produto.append(i)
            i+=1
        else:
            i+=1
    return produto