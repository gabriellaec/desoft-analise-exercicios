def eh_primo(n):
    if n == 2 or n ==3:
        return True
    if n == 0 or n ==1 or n < 0:
        return False
    i = 3
    while i < n:
        if n%i == 0 or n%2 == 0:
            return False
        i = i+2
    else:
        return True
    
def primos_entre(a,b):
    lista = []
    i = a
    while i <= b:
        x = eh_primo(i)
        if a > 0 and x == True:
            lista.append(i)
        i = i+1
    return lista