def eh_crescente (lista):
    a=0
    b=1
    lista1=[]
    while a<len(lista):
        while lista[a]<lista[b]:
            lista1.append(lista[a])
            a+=1
            b+=1
        a+=1
    if len(lista1)==len(lista):
        return True
    else:
        return False
        
    