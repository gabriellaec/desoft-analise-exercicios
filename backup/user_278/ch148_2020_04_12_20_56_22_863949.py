def conta_letras(palavra):
    contagem = {}
    for letra in palavra:
        if letra not in contagem:
            contagem [letra] = 1
        else:
            contagem [letra] += 1
    
    return contagem