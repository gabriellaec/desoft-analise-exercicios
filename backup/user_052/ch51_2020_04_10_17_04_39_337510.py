def primos_entre (a, b):
    primos = [2]
    init = 3
    while init <= b:
        primo = True
        for i in range(len(primos)):
            if init % primos[i] == 0:
                primos = False
        if primo:
            primos.append(init)
        init += 1
    primos_no_intervalo = []
    for i in range(len(primos)):
        if primos[i] >= a:
            primos_no_intervalo.append(primos[i])
    return primos_no_intervalo
