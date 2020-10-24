def eh_primo(p):
    i = 1    
    lista = []
    while i<p+1:
        if p % i == 0:
            lista.append(i)
        i += 1
    if len(lista) == 2:
        return True
    else: return False
        