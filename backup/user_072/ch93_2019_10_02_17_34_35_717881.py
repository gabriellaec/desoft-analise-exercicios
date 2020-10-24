
        
def verifica_numero(n):
    b=repr(n)
    soma=0
    i=0
    while i<len(b):
        soma+=int(b[i])**int(b[i])
        i+=1
    if n==1:
        return False
    if soma==n:
        return True
    else:
        return False
        