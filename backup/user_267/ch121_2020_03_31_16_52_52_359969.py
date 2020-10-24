def subtracao_de_listas(lista_a,lista_b):
    lista=[]
    for i in lista_a:
        if i not in lista_b:
            lista.append(i)
    return lista
   
 