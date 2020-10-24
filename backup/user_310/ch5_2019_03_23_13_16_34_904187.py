def eh_primo(n):
    i=2
    if n==0 or n==1:
        return False
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True


def maior_primo_menor_que(n):
    numero=n
    
    if numero<=1:
        return -1
    
    while numero>1:
        if eh_primo(numero):
            return numero
        numero-=1