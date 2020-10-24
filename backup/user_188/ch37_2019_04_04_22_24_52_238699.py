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
    contador = 0
    valor = 0
    while contador <= numero:
        if eh_primo(valor):
            lista.append(valor)
            valor += 1
            contador += 1
        else:
            valor += 1
    return lista
    