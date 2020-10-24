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

def lista_primos(n):
    lista = []
    x = 1
    while len(lista) + 1  <= n:
        if eh_primo(x):
            lista.append(x)
            
        x += 1
            
    return lista

   

