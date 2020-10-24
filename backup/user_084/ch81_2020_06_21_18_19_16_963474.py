def interseccao_valores(D1,D2):
    valores=[]
    valores_final=[]
    for c in D1:
        valores.append(D1[c])
    for v in D2:
        if D2[v] in valores:
            valores_final.append(D2[v])
        else:
            pass
    return valores_final
    