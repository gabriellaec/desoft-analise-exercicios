def posicoes_minusculas(string):
    minusculas = []
    for i in range(len(string)):
        if string[i].islower():
            minusculas.append(i)
    
    return minusculas