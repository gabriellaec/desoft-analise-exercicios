def subtracao_de_listas(lista1,lista2):
    i=0
    lista_nova=[]
    if len(lista1)==0:
        return lista1
    while i<=len(lista1)-1:
        p=0
        while p<=len(lista2)-1:
            if lista1[i]==lista2[p]:
                del lista1[i]
                p+=1
            else:
                print (lista1)
                p+=1
        i+=1
        return lista1
