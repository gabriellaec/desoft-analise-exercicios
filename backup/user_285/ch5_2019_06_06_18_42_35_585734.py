def eh_primo(n):
    primo=True
    if n<=1:
        primo=False
    for e in range(2,n):
        if n%e==0 and e!=n:
        	primo=False
    return primo

def menor_primo_maior_que(n):
    for i in range(
