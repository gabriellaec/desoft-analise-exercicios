def calcula_pi (n):
    i=1
    soma=0
    while i<len(n+1):
        a = 6/(n**2)
        soma+=a
        i+=1
    return soma