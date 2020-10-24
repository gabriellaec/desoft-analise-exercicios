def apaga_repetidos(stringue):
    letras_usadas = []
    output = ''
    for letra in stringue:
        if letra not in letras_usadas:
            letras_usadas.append(letra)
            output+=letra

        else:
            output+='*'
    return output