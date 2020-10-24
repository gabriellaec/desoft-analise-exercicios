def eh_crescente (lista):
    a=0
    b=1
    lista1=[]
    while a<=len(lista):
        y=lista[a]
        x=lista[b]
        while y<x:
            y=lista[a]
            x=lista[b]
            lista1.append(y)
            a+=1
            b+=1
        a>len(lista)
    if len(lista1)==len(lista):
        return True
    else:
        return False
        
    