def conta_a(palavra):
    contador = 0
    conta_a = 0
    while contador < len(palavra):
        if palavra[contador] == "a":
            conta_a +=1
        contador += 1
    return conta_a