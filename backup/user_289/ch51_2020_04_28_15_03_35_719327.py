def eh_primo (numero):
    if numero == 2:
        return True
    elif numero == 0 or numero == 1:
        return False
    elif numero%2 == 0:
        return False
    else:
        contador = 3
        while contador < numero:
            if numero%contador == 0:
                return False
            contador += 2   
        return True
def primos_entre(a, b):
    lista_p = []
    while a <= b and a > 0:
        if eh_primo(a) == True:
            lista_p.append(a)
            a += 1
        else:
            a += 1
    return lista_p
