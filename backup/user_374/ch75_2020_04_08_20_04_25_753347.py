def eh_primo(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x%2 == 0:
        return False
    k = 3
    while k < x :
        if x%k == 0:
            return False
        else:
            k = k + 2
    return True            

def verifica_primos(lista):
    verificador = {}
    
    for num in lista:
        if eh_primo(num) == True:
            verificador[num] = True
        else:
            verificador[num] = False
    return verificador