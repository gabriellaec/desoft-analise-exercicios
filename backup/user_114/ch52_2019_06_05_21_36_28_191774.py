lista2=[]
def eh_crescente(lista):
    i=0
    while i<len(lista):
        if lista[i+1]>lista[i]:
            lista2.append(lista[i])
    if len(lista2)==len(lista):
        return True
    else:
        return False