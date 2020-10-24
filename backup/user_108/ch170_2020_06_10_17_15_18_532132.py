def apaga_repetidos(palavra):
    letras = set()
    output = ""
    for letra in palavra:
        if letra in letras:
            output+= "*"
        else:
            output+= letra
            letras.add(letra)
    return output