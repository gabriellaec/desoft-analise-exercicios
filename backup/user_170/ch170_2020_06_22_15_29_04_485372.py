def apaga_repetidos(palavra):
    lsWord = []
    word = ""
    for l in range(len(palavra)):
        if palavra[l] not in lsWord:
            lsWord.append(palavra[l])
            word += palavra[l]
        else:
            word += "*"
    return word