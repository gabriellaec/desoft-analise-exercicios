def posicoes_minusculas(string):
    resultado = []
    for i in range(len(string)):
        if string[i].islower():
            resultado.append(i)
    return resultado
   
        
            