def calcula_euler(x,n):
    i=1
    conta=1
    
    while i<n:
        conta=conta+(x**i)/fact(i)
        i+=1
    return conta