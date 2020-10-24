def eh_primo(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True
    if x%2==0:
        return False
    
    tmp = 3
    while tmp < x:
        if x%tmp == 0:
            return False
        else:
            tmp = tmp + 2
    return True

def primos_entre (a, b):
    quantidade_de_primos = 0
    x = a
    while x < b:
        if eh_primo (X):
            quantidade_de_primos += 1
        x +=1
    return quantidade_de_primos

print( primos_entre(2, 5))