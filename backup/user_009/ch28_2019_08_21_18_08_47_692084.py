def velocidade(vel):
    if vel > 80:
        return "você foi multado em: {0}".format((vel-80)*5)
    else:
        return "você não foi multado"