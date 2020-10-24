def calcula_euler(x,n):
    i=1
    e=1
    valor=1
    while1<n and n>1:
        e=e+x**i/valor
        i+=1
        valor=valor+1
    return e