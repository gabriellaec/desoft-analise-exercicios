def eh_primo(n):
    numero = True
    i=2
    while i<n:
        if n%i == 0:   
            numero= False
        i+=1

    return numero