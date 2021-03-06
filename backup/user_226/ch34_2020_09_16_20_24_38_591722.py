def eh_primo(numero):
    if numero == 0 or numero == 1:
        return False
    elif numero == 2 or numero == 3:
        return True
    elif numero % 2 == 0:
        return False
    else:
        i = 3
        while numero > i:
            if numero % i == 0:
                return False
            else:
                i += 1
        if i >= numero:
            return True

def primos_entre(a, b):
    lista = []
    i = a + 1
    if eh_primo(a):
        lista.append(a)
    if eh_primo(b):
        lista.append(b)
    while i < b:
        if eh_primo(i):
            lista.append(i)
        i += 1
    return lista

def maior_primo_menor_que(n):
    if eh_primo(n):
        return n
    elif n < 2:
        return -1
    else:
        lista = primos_entre(2, n)
        return lista[len(lista) - 1]