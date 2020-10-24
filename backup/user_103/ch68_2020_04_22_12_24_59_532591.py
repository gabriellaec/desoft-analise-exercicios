def separa_trios(lista):
    lista_trio=[]
    i=0
    while i< len(lista):
        lista_trio.append(lista[i],lista[i+1],lista[i+3])
        i+=1
        if lista[len(lista)-1]%3==2:
            lista_trio.append(lista[len(lista)-1], lista[len(lista-2)])
        elif lista[len(lista)-1]%3==1:
            lista_trio.append(lista[len(lista)-1])
        i+=1
        
    return lista_trio