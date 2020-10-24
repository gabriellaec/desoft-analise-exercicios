def conta_letras(frase):
    dict = {}
    for letra in frase:
        if letra not in dict:
            dict[letra] = 1
        else:
            dict[letra] += 1
        
    return dict