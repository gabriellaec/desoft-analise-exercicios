def calcula_valor_devido(vemp, nmes, txjuros):
    
    vdev= vemp*((1+txjuros)**nmes)
    return vdev

x=calcula_valor_devido(1000, 2, 5)
print(x)


