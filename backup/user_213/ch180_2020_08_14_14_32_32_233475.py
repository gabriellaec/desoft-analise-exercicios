def ocorrencias_letras(s):
    dici = {}
    for l in s:
        if l in dici:
            dici[l]+=1
        else:
            dici[l]=1
    return dici
            
            
        