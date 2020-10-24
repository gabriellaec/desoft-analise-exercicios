def soma_impares (numeros):
    i=0
    s=0
    while i<len(numeros):
        if numeros[i]%2!=0:
            s+=numeros[i]
            return s
            i+=1        