def calcula_fibonacci(n):
    lista = [0]*n
    lista[0]=1
    lista[1]=1
    i = 2
    if n==0:
        print([])
    elif n==1:
        print([1])
    while i < n:
        lista[i]=lista[i - 1]+lista[i-2]
        i+=1
    return lista
print(calcula_fibonacci(0))