def eh_primo(numero):
    div = 0
    cont = 0
    if numero == 0 or numero == 1:
        return False
    while True:
        div += 1
        if numero % div == 0:
            cont += 1
        if div == numero:
            break
    if cont > 2:
        return False
    return True

def lista_primos(numero):
    primos = []
    cont = 1
    while len(primos) < numero:
        if eh_primo(cont):
            primos.append(cont)
        cont += 1
    
    return sorted(primos)


