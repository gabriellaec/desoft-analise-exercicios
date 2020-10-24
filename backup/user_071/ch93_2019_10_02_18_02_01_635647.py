def verifica_numero(n):
    soma=0
    i=0
    while i<len(n):
        soma=i**i
        i+=1
    if soma==n:
        return 'True'
    if n<1 or soma!=n:
        return 'False'