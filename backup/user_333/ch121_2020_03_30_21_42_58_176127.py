def subtracao_de_listas(lista1,lista2):
    if len(lista1)==0:
        lista1=[]
        return lista1
    elif len(lista2)==0:
        return lista1
    else:
        i=0
        while i<len(lista1):
            j=0
            while j<len(lista2):
                if lista1[i]==lista2[j]:
                    del lista1[i]
                    i-=1
                    break
                j+=1
            i+=1
        return lista1