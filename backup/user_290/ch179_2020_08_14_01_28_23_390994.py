def posicoes_minusculas(s):
    posicoes = []
    for i in range(len(s)):
        if s[i].islower() == True:
            posicoes.append(i)
    return posicoes