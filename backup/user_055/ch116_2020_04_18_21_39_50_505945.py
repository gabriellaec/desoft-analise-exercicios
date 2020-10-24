def raiz_quadrada(n):
    lista_raiz = []
    i = 1
    while n > 0:
        n -= i
        lista_raiz.append(n)
        i += 2
    return len(lista_raiz)
    
        
        