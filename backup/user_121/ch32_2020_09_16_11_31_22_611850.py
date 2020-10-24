def eh_primo(n):
    if n==2:
        resultado=True
    elif n%2==0 or n==1 or n==0:
        resultado=False
    else:
        i=2
        while i<n:
            if n%i==0:
                resultado=False
                break
            else:
                i+=1
            resultado=True
    return resultado

def lista_primos(n):
    primos=[]*n
    i=0
    while i<=n:
        if eh_primos(n)==True:
            primos.append(i)
        else:
            continue
    i+=1
    return primos