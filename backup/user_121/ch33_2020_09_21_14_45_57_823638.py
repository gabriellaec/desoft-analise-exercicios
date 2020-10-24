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
    contador=0
    while a<=b:
        if eh_primo(a)==True:
            contador+=1
        a+=1
    return contador