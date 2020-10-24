def quantos_uns (numero):
    contador=0
    i=0
    while i<len(numero):
        i=i+1
        if numero[i]==1:
            contador=contador+1
            return contador 