def conta_a(numero):
    passador = 0
    contador = 0
    palavra = str(numero)
    letra = len(palavra)
    while passador <= letra:
        passador += 1
        if passador[letra] == "a":
            contador += 1
    return (contador)