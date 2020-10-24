def eh_primo(n):
    if n == 2 or n ==3:
        return True
    if n == 0 or n ==1:
        return False
    i = 3
    while i < n:
        if n%i == 0 or n%2 == 0:
            return False
        i = i+2
    else:
        return True
    
def verifica_primos(lista):
    dict = {}
    for i in lista:
        dict[i] = []
        if eh_primo(i) == True:
            dict[i] = [True]
        if eh_primo(i) == False:
            dict[i] == [False]
    return dict
            