def quantos_uns (numero):
    contador=0
    i=0
    while i<len(numero):
        if numero[i]==1:
            contador=contador+1
        i+=1
    return contador 
        