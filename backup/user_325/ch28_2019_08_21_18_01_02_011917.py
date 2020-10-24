def velocidade(v):
    if v > 80:
        m = (v - 80) * 5
        return("voce foi multado {0:.2f}".format(m))
    else:
        return("Não foi multado")
print(velocidade(88))