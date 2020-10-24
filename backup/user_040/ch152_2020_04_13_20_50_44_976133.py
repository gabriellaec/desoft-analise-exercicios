def verifica_preco(x,y,z):
    dic1 = {}
    dic2 = {}
    for x, cor in y.items():
        dic1[x] = cor
    for cor2, valor in z.items():
        dic2[cor2] = valor
        
    if dic1[x] == cor2:
        return cor2
        
    