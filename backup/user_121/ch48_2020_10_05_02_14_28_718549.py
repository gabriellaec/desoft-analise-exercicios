def eh_crescente(lista):
    lista_teste=[]
    i=1
    while i<len(lista):
        if lista[i]>lista[i-1]:
            lista_teste.append(lista[i-1])
        else:
            lista_teste.clear()
        i+=1
    if len(lista_teste)>0:
        return True
    else:
        return False