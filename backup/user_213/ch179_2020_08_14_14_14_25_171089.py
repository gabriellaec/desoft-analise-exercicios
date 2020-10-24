def posicoes_minusculas(s):
    min = []
    for i in range(len(s)-1):
        if s[i].islower() == True:
            min.append(i) 
    return min