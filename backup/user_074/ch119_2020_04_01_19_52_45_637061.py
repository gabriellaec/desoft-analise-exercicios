def calcula_euler(x,n):
    i=0
    x=0
    resultado=1
    for b in range(1,numero+1):
        resultado *= b
    while i<n:
        x+=2**i/resultado
        i+=1
        e**x=x*(2**i/resultado)
    return(e)