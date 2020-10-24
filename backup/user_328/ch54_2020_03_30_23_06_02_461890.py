def calcula_fibonacci(n):
    f1=1
    f2=1
    contador=3
    n= len(n)
    while contador<= n:
        f3= f1+f2
        f1=f2
        f2=f3
    return n