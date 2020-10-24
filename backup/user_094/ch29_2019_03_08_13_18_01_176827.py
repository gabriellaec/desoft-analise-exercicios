def calcula_aumento (satual):
    if satual>=1250:
        aumento= satual*1.1
        return aumento
    else:
        aumento= satual + satual*15/100
        return aumento