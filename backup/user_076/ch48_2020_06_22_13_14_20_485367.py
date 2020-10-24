def eh_crescente (lista):
    i=0
    c=0
    while i<len(lista):
        while c<i:   
            if lista[i+1]<lista[i-c]:
                crescente = False
            c+=1
        i+=1
    return crescente