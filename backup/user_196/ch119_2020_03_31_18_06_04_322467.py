def calcula_euler(x,n):
    i = 0
    fatorial = 1
    e = 1 
    euler = 0
    while i < n:
        euler += (x**i)/fatorial
        i+=1
        fatorial+=1
    return euler