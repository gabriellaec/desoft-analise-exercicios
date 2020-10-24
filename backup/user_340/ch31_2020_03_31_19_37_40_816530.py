0==False
1==False
def eh_primo(numero):
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
        