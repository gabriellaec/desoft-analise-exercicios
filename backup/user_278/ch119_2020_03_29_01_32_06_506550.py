def calcula_euler(x,n):
    i=1 #contador
    e=1
    valor=1
    while i<n and n>1:
        e = e + x**i/valor
        i+=1
        valor = valor * i