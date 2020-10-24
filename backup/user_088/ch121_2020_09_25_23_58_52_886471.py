def subtracao_de_listas(lista1,lista2):
    i=0
    lista3=[]
    while(i<len(lista1) or i<len(lista2) ):
        if(lista1[i] not in lista2):
            lista3.append(lista1[i] or lista2[i])
        i+=1    
        return (lista3)
         