def posicoes_minusculas(s):
    i=0
    lista_indices = []
    while i<len(s):
        letra = s[i]
        if letra.islower() == True:
            lista_indices.append(i)
        i+=1
        
    return lista_indices