def verifica_primo(n):
    primo=True
    i=2
    while i<n:
        if n%i==0:
            primo=False
        i+=1
    return primo

def maior_primo_menor_que(n):
    verifica_primo(n)
    if primo=False:
        i=n
        while i>1:
            while i<n:
                if n%i==0:
                    i-=1
                return i
        return -1
        