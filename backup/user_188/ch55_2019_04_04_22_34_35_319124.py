def eh_primo(numero):
    if numero < 2:
        return False
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1
    return True

def primos_entre(a, b):
    lista = []
    p = a
    while p <= b:
        if eh_primo(p):
            lista.append(p)
        p += 1
    return lista