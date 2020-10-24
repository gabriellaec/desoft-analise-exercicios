def eh_primo(numero):
    if numero==1 or numero==0:
        return False
    if numero==2 or numero==3:
        return True
    y=(numero%2)
    if y==0:
        return False
    if y!=0:
        i=3
        y=(numero%i)
        while y!=0:
            y=(numero%i)
            i+=2
            i<numero
            if y==0:
                return False
            if y!=0:
                return True