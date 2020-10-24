def verifica_preco(x,y,z):
    dic1 = {}
    dic2 = {}
    for x, cor in y.items():
        dic1[x] = cor
    for cor2, valor in z:
        dic2[cor2] = valor
        
    if cor == cor2:
        return valor
        
    