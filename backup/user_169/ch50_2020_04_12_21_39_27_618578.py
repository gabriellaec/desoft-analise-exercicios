def junta_nome_sobrenome(lista1,lista2):
    i=0
    lista3=[]
    
    for i in range(len(lista1)):
                   lista3.append(lista1[i]+''+lista2[i])
                   
    return lista3