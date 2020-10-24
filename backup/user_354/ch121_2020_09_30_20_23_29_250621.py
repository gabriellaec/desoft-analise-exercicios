def subtracao_de_listas(lista,lista_2):
    x=[]
    i=0
    while i<len(lista):
        if lista[i] not in lista_2:
            x.append(lista[i])
       
        i+=1