def eh_crescente(lista):
    i = 0
    crescente = True
    while i <  (len(lista) - 1):
        if lista[i+1] > lista[i]:
            i += 1
            crescente = True        
        else:
            crescente = False
            i = 5
    return crescente

a = [2, 3, 10, 5, 8]
b = eh_crescente(a)

print(b)