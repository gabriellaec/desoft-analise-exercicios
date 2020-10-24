def alunos_impares(lista):
    lista_vazia=[]
    while cont<len(lista):
        lista_vazia.append(lista[0::2])
        cont+=1
    return lista_vazia