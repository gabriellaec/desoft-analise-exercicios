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
def lista_primos(n):
    i = 0
    lista = []
    while len(lista) < n:
        if eh_primo(i) == True:
            lista.append(i)
            i += 1
        else:
            i += 1
    return lista