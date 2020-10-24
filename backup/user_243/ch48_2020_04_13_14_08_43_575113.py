def eh_crescente(lista):
    if lista=[] or len(lista)=1:
        return True
    i=1
    a=1
    while len(lista)>i:
        if lista[i]>lista[i-a]:
            return True
        else:
            return False
    i+=1
    a+=1