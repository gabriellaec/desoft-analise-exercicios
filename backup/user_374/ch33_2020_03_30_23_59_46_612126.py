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

def primos_entre(a,b):
    quantidade_de_primos = 0 
    x = a
    while x < b:
        if eh_primo(x):
            quantididade_de_primos =+ 1
        x += 1
    return quantidade_de_primos