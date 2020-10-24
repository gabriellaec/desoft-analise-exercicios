def eh_primo(n):
    primo=True
    if n<=1:
        primo=False
    for e in range(2,n):
        if n%e==0 and e!=n:
        	primo=False
    return primo
lista_primos=[]
def maior_primo_menor_que(n):
    if n<=0:
        return -1
    else:
        for i in range(0,n+1):
            if eh_primo(i):
                lista_primos.append(i)
                maiorprimo=lista_primos[-1]
        return maiorprimo
