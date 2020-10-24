lista1=[10,12,5,1]
def monta_mala(lista1):
    lista2 = []
    i=0
    j=1
    f=
    d=len(lista1)
    if d>=1:
        while j<len(lista1):
            a=lista1[i]
            b=lista1[j]
            if a<23:
                c=a+b
                if c<23:
                    lista2.append(a)
                    lista2.append(b)
                    i+=2
                    j+=2
                    x=sum(lista2)
                    if  x<23:
                        break 
    if lista1[i]+x<=23:
        lista2.append(lista1[i])
            
    return lista2