
def calcula_euler(x,n):
    a=1
    e=1
    valor=1
    while a<n and n>a:
        e= e + x**a/valor
        a += 1
        valor = valor + a
    return(e)