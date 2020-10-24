def eh_primo(numero):
    impar=3
    if numero==0 or numero==1:
        return False 
    if numero==2:
        return True 
    if numero%2==0:
        return False 
    while numero>impar:
        if numero%impar==0:
            return False 
        impar+=2
    return True 
    