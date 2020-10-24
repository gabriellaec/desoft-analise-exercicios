def conta_a(p):
    contador = 0
    quantos = 0
    while contador < len(p):
        if p[contador] == "a":
            contador += 1
            quantos += 1
        else:
            contador +=1
    return quantos
