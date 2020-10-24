def calcula_fibonacci (n):
    
    lista_fibo = []
    
    if n == 0:
        return lista_fibo
    elif n == 1:
        lista_fibo.append(1)
        return lista_fibo
    elif n == 2:
        lista_fibo.append(1)
        lista_fibo.append(1)
        return lista_fibo
    else:
        lista_fibo.append(1)
        lista_fibo.append(1)
        i = 2
        while len(lista_fibo) < n:
            novo = lista_fibo[i-2] + lista_fibo[i-1]
            lista_fibo.append(novo)
            i += 1
            
    return lista_fibo
    