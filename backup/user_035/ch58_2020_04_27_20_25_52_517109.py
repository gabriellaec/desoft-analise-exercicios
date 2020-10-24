def conta_a(string):
    contador = 0
    e = 0
    while e <= len(string):
        if string[e] == "a":
            contador += 1
            e += 1
        else:
            e += 1
    return contador