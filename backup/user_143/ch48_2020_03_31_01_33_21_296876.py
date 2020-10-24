def eh_crescente (lista):
    a=0
    b=1
    lista1=[]
    while b<=len(lista):
        y=lista[a]
        x=lista[b]
        if y<x:
            lista1.append(y)
            a+=1
            b+=1
        if len(lista1)==len(lista):
            return True
        else:
            return False
        
    