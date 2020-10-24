def conta_a (string):
    contador = 0
    vezes_a=0
    while contador < len(string):
        if string[contador] == "a":
            vezez_a += 1
        contador += 1
    return vezes_a