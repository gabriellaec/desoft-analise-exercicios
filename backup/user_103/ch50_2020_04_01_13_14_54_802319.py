def junta_nome_sobrenome(lista1,lista2):
    i=0
    lista=[]
    while i < len(lista1):
        soma= (lista1[i])+(' ')+(lista2[i])
        i+=1
        lista.append(soma)
    return lista