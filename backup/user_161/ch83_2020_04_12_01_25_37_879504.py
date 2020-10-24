def medias_por_inicial(entrada):
    letras = {}
    for nome in entrada:
        if nome[0] in letras:
            letras[nome[0]].append(entrada[nome])
        else:
            letras[nome[0]] = [entrada[nome]]
    
    for letra in letras:
        if len(letras[letra]) > 1:
            letras[letra] = (letras[letra][0] + letras[letra][1])/2
        else:
            letras[letra] = letras[letra][0]
    
    return letras