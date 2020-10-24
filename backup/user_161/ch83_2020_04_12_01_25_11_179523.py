def medias_por_inicial(entrada):
    letras = {}
    for nome in entrada:
        if nome[0] in letras:
            letras[nome[0]].append(entrada[nome])
        else:
            letras[nome[0]] = [entrada[nome]]
    
    for letra in letras:
        tamanho = len(letras[letra])
        soma = 0
        for letra_soma in letras[letra]:
            soma += letra_soma
        letras[letra] = soma/tamanho

    return letras
