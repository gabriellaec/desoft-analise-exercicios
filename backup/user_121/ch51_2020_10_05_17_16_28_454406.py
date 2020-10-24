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

def primos_entre(a, b):
    lista_final=[]
    i=a
    while i<=b:
        if eh_primo(i)==True:
            lista_final.append(i)
        else:
            continue
        i+=1
    return lista_final