def eh_primo(numero):
    if numero <= 1:
        return False
    if (numero % 2 == 0 or numero % 3 == 0):
        return False
    if numero <= 3:
        return True
    i=5
    while i <= 9:
        if numero % i == 0:
            return False
            i+=2
        elif numero % i != 0:
            return True
        
