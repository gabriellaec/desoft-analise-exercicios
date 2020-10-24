def calcula_euler(x,n):
    i= 1
    lista=[1]
    soma= 1
    a= 1
    while i < n:
        if n != 0:
            lista.append((x**i)/a)
            a= a*n
            soma= soma + lista[i]
            n= n - 1
            i= i + 1
        
        else:
            break
    return soma


    
        