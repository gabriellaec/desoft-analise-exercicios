def eh_primo(numero):
    if numero < 2:
        return False
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1
    return True

def imprime_primos(numero):
    lista = []
    for valor in range(numero + 1):
        if eh_primo(valor):
            lista.append(valor)
    return lista
    