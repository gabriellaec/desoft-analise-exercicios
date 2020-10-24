def eh_crescente (lista):
    i=1
    crescente = True
    while i<len(lista):
        c=1
        while c<i:   
            if lista[i]<lista[i-c]:
                crescente = False
            c+=1
        i+=1
    return crescente