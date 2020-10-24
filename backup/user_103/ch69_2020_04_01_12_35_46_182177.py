def junta_listas(lista):
    lista1=[]
    i=0
    while i< len(lista):
        lista1.append(str(lista[i]).strip('[]'))
        i+=1
        a=','.join(lista1).replace("'", "")
    return a

  