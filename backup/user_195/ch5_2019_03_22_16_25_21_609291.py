def verifica_primo(n):
    primo=True
    i=2
    while i<n:
        if n%i==0:
            primo=False
        i+=1
    return primo

def maior_primo_menor_que(n):
    if verifica_primo(n):
        return n
    else:
        while n>1:
            n-=1
            if verifica_primo(n):
                return n
            else:
                return "-1"
        