def calcula_aceleracao(r, rpm):
    f = rpm/60
    return ((2*math.pi*f)**2)*r