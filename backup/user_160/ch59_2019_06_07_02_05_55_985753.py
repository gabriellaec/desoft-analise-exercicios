def conta_a(n):
    soma = 0
    for i in range(0,len(n)):
        if  n[i] == "a":
            soma = soma + 1
    return soma