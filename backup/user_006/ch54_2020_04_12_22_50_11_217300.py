def calcula_fibonacci(n):
    valores=[1,1]
    i=0
    while n-2!=0:
        valores[i+2]=valores[i]+valores[i+1]
        n=n-1
        i=i+1
    return valores