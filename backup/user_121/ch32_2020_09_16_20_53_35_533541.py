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
    lista=[]
    j=2
    while j<=n:
        if eh_primo(n)==True:
            lista.append(j)
        else:
            continue
        j+=1
    return lista