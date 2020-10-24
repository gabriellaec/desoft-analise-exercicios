def velocidade(vel):
    if vel > 80:
        m = (v - 80) * 5
        return("voce foi multado em: {0}".format((vel - 80) * 5)
    else:
        return("Não foi multado")
print(velocidade(88))