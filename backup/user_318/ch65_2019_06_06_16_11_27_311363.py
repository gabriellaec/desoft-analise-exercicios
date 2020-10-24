def acha_bigramas(string):
    lista=[]
    i=0
    while i<len(string):
        lista.append(string[i:i+2])
        i+=1
    if len(string) % 2 != 0:
        del(lista[-1])
        del(lista[2])
    return lista
