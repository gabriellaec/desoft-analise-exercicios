def conta_a(string):
    i = 0
    soma = 0
    while i < len(string):
        if string[i] == "a":
            soma += 1
        i += 1
    return soma