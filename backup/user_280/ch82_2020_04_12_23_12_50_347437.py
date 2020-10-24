def primeiras_ocorrencias(palavra):
    dicionario = {}
    babu = list(palavra)
    i=0
    while i < len(babu):
        for letra in palavra:
            if letra == babu[i]:
                dicionario[letra] = i
        i+=1
    return dicionario
    