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