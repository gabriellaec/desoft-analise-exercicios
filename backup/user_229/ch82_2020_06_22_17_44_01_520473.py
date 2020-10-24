def primeiras_ocorrencias(string):
    caract_1 = {}
    for i in range(len(string)):
        if string[i] not in caract_1:
            caract_1[caract] = i
            
    return caract_1