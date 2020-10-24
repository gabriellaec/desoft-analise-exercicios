def calcula_fibonacci(n):
    f1=1
    f2=1
    contador=3
    tamanho= len(n)
    while contador <= tamanho:
        f3= f1+f2
        f1=f2
        f2=f3
    return n