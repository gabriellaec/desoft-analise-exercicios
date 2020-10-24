def eh_crescente (lista):
    a=1
    n=len(lista)
    while a<n:
        if lista[a-1]<lista[a]:
            a+=1
        else:
            return False
    return True
        
    