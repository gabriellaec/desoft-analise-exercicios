def eh_primo(teste):
    if teste==2:
        resultado=True
    elif teste%2==0 or teste==1 or teste==0:
        resultado=False
    else:
        i=2
        while i<teste:
            if teste%i==0:
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
        if resultado==True:
            primos.append(i)
        else:
            continue
    i+=1
    return primos