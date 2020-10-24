def conta_a (numero):
    contador = 0
    passador = 0
    palavra = str(numero)
    while passador < len(palavra):
        if palavra[passador] == "a":
        	contador += 1
        passador += 1
    return contador