def verifica_numero(n):
    soma=0
    for i in n:
        soma=i**i
    if soma==n:
        return 'True'
    if n<1 or soma!=n:
        return 'False'