def posicoes_minusculas(s):
    min = []
    for i in range(len(s)):
        if s[i].islower() == True:
            min.append(i) 
    return min