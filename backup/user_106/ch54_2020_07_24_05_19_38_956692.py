def calcula_fibonacci(n):
    lista_f = [1, 1]
    i = 0
    f1 = 1
    f2 = 1
    
    if n == 0:
        return []
    
    elif n == 1:
        return [1]

    else:
        while i < n-2:
            s = f1 + f2
            lista_f.append(s)
            f1 = f2
            f2 = s
            i += 1
        return lista_f