def eh_primo(teste):
    if teste%2==0 or teste==0 or teste==1:
        resultado=False
    else:
        i=1
        while i<teste:
            if teste%i==0:
                resultado=False
                i+=1
            else:
                resultado=True
                i+=1
            i+=1
    return resultado