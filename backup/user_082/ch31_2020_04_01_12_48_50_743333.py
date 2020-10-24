def eh_primo(numero):
    i=3
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0:
        return False
    while (i) <= numero:
        if numero % i == 0 and numero == i:
            return True
        
        if numero % i !=0 and numero != i:
            return False
        i+=1