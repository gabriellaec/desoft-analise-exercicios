def eh_primo(numero):
    i=3
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0:
        return False
    while (i) <= numero:
        if numero % i == 0 and numero == i:
            return True
        
        elif numero % i !=0 or numero != i:
            return False
        i+=1