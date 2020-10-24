def apaga_repetidos(texto):
    cripto = ''
    for letra in texto:
        if letra in cripto:
            letra = '*'
        cripto += letra
    return cripto