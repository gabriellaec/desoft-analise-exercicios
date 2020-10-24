def primeiras_ocorrencias(palavra):
    posicao=0
    dici={}
    for letra in palavra:
        posicao+=1
        if letra not in dici:
            dici[letra]=posicao
    return dici
            