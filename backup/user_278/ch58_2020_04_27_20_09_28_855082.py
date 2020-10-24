def conta_a (palavra):
    tam = len(palavra)
    contador = 0
    for i in tam:
        if palavra [i]=="a":
            contador+=1
    return contador