def calcula_euler(x,n):
    a= 1
    while True:
        if n != 0:
            a= a*n
            n= n -1
        else:
            break
    i= 0
    lista=[1]
    soma= 0
    while i < n:
        lista.append((x**i)/a)
        soma= soma + lista[i]
        i= i + 1
    return soma
    
        