def conta_a(palavra):
    contador = 0
    for i in palavra:
        if i == "a":
            contador = contador + 1
    return contador
print(conta_a("paralelepipedo"))
