def calcula_pi (n):
    i=1
    soma=0
    while i<len(n):
        a = 6/(n**2)
        soma+=a
        i+=1
        return soma