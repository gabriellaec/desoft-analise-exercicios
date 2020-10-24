def subtracao_de_listas (lista1,lista2):
    lista=[]
    for termo1 in lista1:
        for termo2 in lista2:
            
            if termo1!=termo2:
                if termo1 not in lista:
                    lista.append (termo1)
            elif termo1==termo2:
                if termo1 in lista:
                    for i,e in enumerate(lista):
                        if e==termo1:
                            posicao=i
                    del lista[posicao]
                break
    return lista