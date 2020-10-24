def calcula_euler(x,n):
    i=1
    conta=1
    while i<n:
        conta=conta+(x**i)/i*(i-1)*(i-2)*(i-3)
        i+=1
    return conta