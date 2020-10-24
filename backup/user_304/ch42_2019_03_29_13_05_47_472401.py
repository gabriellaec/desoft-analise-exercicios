def quantos_uns (numero):
    palavra=str(numero)
    contador=0
    i=0
    while i<len(palavra):
        if palavra[i]=='1':
            contador=contador+1
        i+=1
    return contador 
        