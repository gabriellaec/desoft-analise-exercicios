def calcula_fibonacci(n):
    valores=[1,1]
    i=0
    while i<(n-2):
        valores[i+2]=valores[i]+valores[i+1]
        i=i+1
    return valores