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

def maior_primo_menor_que(n):
    lista = []
    x = 1
    contagem = 0
    while x <= n:
        if eh_primo(x):
            lista.append(x)
            contagem += 1
            
        x += 1
            
    return lista[contagem-1]