def posicoes_minusculas(s):
    posicoes = [1]
    for i in range(len(s)):
        if s[i].islower() == True:
            posicoes.append(i)
    return posicoes