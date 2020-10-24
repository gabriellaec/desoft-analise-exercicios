def eh_primo(numero):
    impar=3
    if numero==2:
        return True
    if numero%2==0:
        return False
    while impar<numero:
        if numero%impar==0:
            return False
        impar+=2
    return True