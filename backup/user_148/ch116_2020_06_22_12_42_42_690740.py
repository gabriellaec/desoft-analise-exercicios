def raiz_quadrada(n):
    lista = []
    sub = 1
    
    while sub>0:
        sub = n - sub
        lista.append(sub)
        sub += 2
        
    return len(lista)