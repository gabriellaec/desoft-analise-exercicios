numeros=[]
def inverte_lista(numeros):
    lista_nova=[]
    i=1
    while i<=len(numeros):
        lista_nova.append(numeros[-i])
        i+=1
    return lista_nova