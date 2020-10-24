def ver_munchhaunsen(a):
    lista=[]
    b= str(a)

    i=0
    while i<len(b):
        lista.append(b[i])
        i+=1


    soma =0
    e=0
    while e<len(lista):
        soma+= int(lista[e])**int(lista[e])
        e+=1
        
    if a == soma:
        return True
    elif a<0:
        return False
    else:
        return False