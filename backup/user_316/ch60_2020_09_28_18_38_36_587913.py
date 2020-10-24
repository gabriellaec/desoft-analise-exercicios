def eh_palindromo(t):
    # DESAFIO 1
    if t == t[::-1]:
        return True
    return False

def eh_palindromo2(t):
    # DESAFIO 2
    inverso = ''
    
    for i in reversed(range(len(t))): # [::-1]
        inverso += t[i]
        print(inverso)
    if inverso == t:
        return True
    
    return False