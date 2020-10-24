def apaga_repetidos(string):
    separado = list(string)
    for c in separado:
        if c in separado:
            c = '*'
    texto = separado.join()
    return texto