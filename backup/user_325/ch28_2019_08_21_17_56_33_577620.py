def velocidade(v):
    if v > 80:
        m = (80 - v) * 5
        print("voce foi multado em {0:.2f} reais".format(m))
    else:
        print("nao foi multado")