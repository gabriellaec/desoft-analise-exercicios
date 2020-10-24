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
    j=0
    while len(lista)<n:
        if eh_primo(j)==True:
            lista.append(j)
        j+=1
    return lista