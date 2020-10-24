def raiz_quadrada(n):
    lista = []
    sub = 1
    
    while n>0:
        n -= sub
        lista.append(sub)
        sub += 2
        
    return len(lista)