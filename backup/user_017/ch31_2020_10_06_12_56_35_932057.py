def eh_primo(n):
    numero = True
    i=3
    if n==0 or n==1:
        numero=False
    while i<n:
        if n%2==0:
            numero=False
        elif n%i == 0:   
            numero= False
            
        i+=2
    return numero
