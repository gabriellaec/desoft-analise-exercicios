def junta_listas(lista):
    lista1=[]
    i=0
    while i< len(lista):
        lista3=lista1.append(str(lista[i]).strip('[]'))
        i+=1
        a=' '.join(lista3)
    print (lista3)
