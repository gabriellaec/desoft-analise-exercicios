def inverte_lista (lista):
    invertida=[]
    i=0
    while i<len(lista)-1:
        invertida.append (len(lista)-1-i)
        i+=1
    return invertida
        