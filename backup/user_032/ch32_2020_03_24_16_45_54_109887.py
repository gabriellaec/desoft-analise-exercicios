def eh_primo(numero):
    if numero == 0 or numero == 1:
        return False
    if numero == 2:
        return True
    if numero %2 == 0:
        return False
    div = 3
    while numero > div:
        if numero %div == 0:
            return False
        div= div + 1
    return True
def lista_primos(n):
    contador = 1
    numero = 1
    lista = []
    while contador <= n:
        if eh_primo(numero):
            lista.append(numero)
            contador = contador + 1
        numero = numero + 1
    return lista