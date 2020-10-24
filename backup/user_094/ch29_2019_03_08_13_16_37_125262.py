def calcula_aumento (satual):
    if satual>=1250:
        satual= satual*1.1
        return satual
    else:
        satual= satual + satual*15/100
        return satual