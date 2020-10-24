def lista_primos(numero):
    if numero == 0 or numero == 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    div = 3
    while numero > div:
        if numero % div == 0:
            return False
    return True
def lista_primos(n):
    contador = 1
    numero = 1
    lista =[]
    while contador <= n:
        if eh_primo(numero):
            lista.append(numero)
            contador = contador+ 1
        numero = numero + 1 
    return lista
        