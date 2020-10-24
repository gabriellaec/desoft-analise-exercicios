def eh_crescente (lista):
    crescente = True
    i = 0
    c = 0
    while i+1<len(lista):
        while c<i:
            if lista[i+1]<lista[i-c]:
                crescente == False
                break
            c+=1
        i+=1
    return crescente
        