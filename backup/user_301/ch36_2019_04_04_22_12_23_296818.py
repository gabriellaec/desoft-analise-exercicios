def eh_primo(numero):
    if numero ==0 or numero==1:
        return False
    if numero%2==0 and numero!=2:
        return False
    if numero==2:
        return True
    c=3
    while c<numero:
        if numero%c==0:
            return False
        c+=2
    return True

        