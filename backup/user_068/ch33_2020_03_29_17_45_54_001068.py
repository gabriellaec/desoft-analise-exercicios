def eh_primo(p):
    if p == 0 or p==1:
        return False
    while c in range(2, p):
        if p % 2 != 0 or p == 2:
            if p % c == 0:
                return False
    return True
def primos_entre(a,b,p):
    lista = []
    for p in range (a, b):
        return lista