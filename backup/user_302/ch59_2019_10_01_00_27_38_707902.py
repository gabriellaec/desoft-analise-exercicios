def conta_a(string):
    i = 0
    contador = 0
    while i < len(string):
        if string[i] == "a":
            contador += 1
        i += 1
    return contador