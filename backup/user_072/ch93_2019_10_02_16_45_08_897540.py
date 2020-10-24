def verifica_numero(n):
    soma=0
    i=0
    while i<len(str(n)):
        soma+=n[i]**int(n)
        i+=1
        if soma==n:
            return True
        