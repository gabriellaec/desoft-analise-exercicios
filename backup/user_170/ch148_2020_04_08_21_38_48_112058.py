def conta_letras(word):
    contagem = {}
    for letra in word:
        if not letra in contagem:
            contagem[letra] = 1
        else:
            contagem[letra] +=1
    return contagem