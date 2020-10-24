def subtracao_de_listas(lista1,lista2):
    lista=[]
    a=len(lista1)
    b=len(lista2)
    #quantide de numeros lista 1 ja testado:
    x=0
    while x<a:
        #quantidade de numeros lista 2 ja testado:
        y=0
        #não tem nenhum elemento da lista2 igual a lista1[x]
        d=0
        while y<b:
            if lista1[x]!=lista2[y]:
                d+=1
                y+=1
            else:
                y+=1
        if  d==b:
            lista.append(lista[x])
            x+=1
        else:
            x+=1
    return lista