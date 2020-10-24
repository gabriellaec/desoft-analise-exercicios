def inverte_lista(lista):
    invertida=[]
    i=0
    tamanho=len(lista)
    while(tamanho>i):
        invertida.append(lista[tamanho-1])
        tamanho-=1
    return invertida