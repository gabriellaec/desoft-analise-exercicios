def primeiras_ocorrencias(string):
    caract_qtd = {}
    for caract in string:
        if caract not in caract_qtd:
            caract_qtd[caract] = 1
        else:
            caract_qtd[caract] += 1
    
    return caract_qtd