def posicoes_minusculas(s):
    listaminu = []
    i = 0
    numero = 0
    while i < len(s):
        if s[i].islower() == True:
            listaminu.append(numero)
            numero +=1
            i+=1
        else:
            numero += 1
            i+=1
    return listaminu
        
        