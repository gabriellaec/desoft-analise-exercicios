def lista_caracteres(palavra):
    caracteres = []
    for letra in palavra:
        if letra not in caracteres:
            caracteres.append(letra)
    return caracteres