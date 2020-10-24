def soma_impares(lista):
    s=0
    i=0
    while i<len(lista):
        if i%2!=0:
            s+=i
            i+=1
    return s
