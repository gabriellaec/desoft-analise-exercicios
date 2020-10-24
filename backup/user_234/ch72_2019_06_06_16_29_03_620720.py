def lista_caracteres(string):
    caract = []
    i=0
    while i < len(string):
        if string[i] not in caract:
            caract.append(string[i])
            i+=1
        else:
            i+=1
    return caract