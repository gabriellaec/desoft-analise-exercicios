def posicoes_minusculas(w):
    resultado = []
    for i in range(len(w)):
        if w[i].islower():
            resultado.append(i)
    return resultado