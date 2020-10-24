def eh_crescente(lista):
    i = 0
    crescente = True
    while lista[i+1] > lista[i]:
            i += 1
            crescente = True        
    if lista[i+1] <= lista[i]:
        crescente = False
           
    return crescente

a = [2, 3, 10, 5, 8]
b = eh_crescente(a)

print(b)