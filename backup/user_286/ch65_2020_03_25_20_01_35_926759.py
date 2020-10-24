def capitaliza(frase):
    frase_listada = list(frase)
    frase_listada[0] = frase_listada[0].upper()
    frase = ''.join(frase_listada)

    return frase
