def conta_a(palavra):
    contador = 0
    i = 0
    for i in palavra:
        if palavra[i] == 'a' or palavra[i] == 'A':
            contador += 1
    return contador 