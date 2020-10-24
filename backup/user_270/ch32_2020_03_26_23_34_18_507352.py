def lista_primos(n):
    lista = []
    t = 2
    if n == 2 :
        lista.append(2)
    elif n > 2:
        while t < n :
            if n % t != 0:
                lista.append(n)
                t += 1
    return lista
        
            
        