def conta_a (palavra):
    tam = len(palavra)
    contador = 0
    for i in range (0,tam):
        if palavra [i]=="a":
            contador+=1
    return contador