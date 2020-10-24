def calculate_valor_devido(vemp, nmes, txjuros):
    
    vdev= vemp*((1+txjuros/100)**nmes)
    return vdev

x=calculate_valor_devido(100, 2, 5)
print(x)


