def junta_nome_sobrenome(lista,lista2):
    lista3 = []
    i = 0
    k=' '
    while i < len(lista):
        lista3.append(lista[i]+k+lista2[i])
        i +=1
    return lista3
        
    