def junta_nome_sobrenome(lista_1, lista_2):
    lista_3=[]
    i=0
    while i<len(lista_1):
        lista_3.append(lista_1[i]+''+lista_2[i])
        i+=1
    return lista_3

        
        