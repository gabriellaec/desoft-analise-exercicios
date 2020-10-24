def eh_primo(numero):
    if numero==1 or numero==0:
        return False
    elif numero==2 or numero==3:
        return True
    else:
        y=(numero%2)
        if y==0:
            return False
        i=3
        while y!=0 and i<numero:
            y=(numero%i)
            i=i+2
        if y!=0:
            return True
        if y==0:
            return False