def soma_valores(lista):
    i = 0
    s = 0
    while i < len(lista):
        s+=lista[i]
        i+=1
    return s
    
print (soma_valores([1,2,3,4,5]))