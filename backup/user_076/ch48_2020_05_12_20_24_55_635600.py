def eh_crescente (lista):
    crescente = True
    i=0
    while i<len(lista):
        j=0
        while j<=i:
            if lista[i+1]<lista[i-j]:
                crescente = False
                break 
            j+=1
        i+=1
    return crescente