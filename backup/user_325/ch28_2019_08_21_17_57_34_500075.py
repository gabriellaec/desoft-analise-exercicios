def velocidade(v):
    if v > 80:
        m = (v - 80) * 5
        print("voce foi multado em {0:.2f} reais".format(m))
    else:
        print("Não foi multado")
    return velocidade