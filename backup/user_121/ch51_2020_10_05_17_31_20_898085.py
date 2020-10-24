def eh_primo(teste):
    if teste==2:
        dale=True
    elif teste%2==0 or teste==1 or teste==0:
        dale=False
    else:
        i=2
        while i<teste:
            if teste%i==0:
                dale=False
                break
            else:
                i+=1
            dale=True
    return dale

def primos_entre(a, b):
    lista_primos=[]
    for p in range(a, b):
        if eh_primo(p)==True:
            lista_primos.append(p)
        else:
            continue
    return lista_primos