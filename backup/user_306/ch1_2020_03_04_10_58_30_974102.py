def calcula_valor_devido(vF, vI, j, k, nT):
    if k > 0 :
        vF = vI*(1+j/k)**nT
    return vf