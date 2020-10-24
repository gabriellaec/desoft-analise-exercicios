def subtracao_de_listas(lista1,lista2):
    i=0
    lista_nova=[]
    while i<len(lista1):
        p=0
        while p<len(lista2):
            if lista1[i]==lista2[p]:
                del lista1[i]
                p+=1
            else:
                p+=1
        i+=1
        return lista1