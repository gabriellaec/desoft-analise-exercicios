def lista_caracteres(frase):
    caracteres = []
    contador = 0
    while contador < len(frase):
        if frase[contador] not in caracteres:
            caracteres.append(frase[contador])
        contador += 1
    return caracteres