def passagem(km):
    if km > 200:
        return "o valor da passagem é de: {0}".format((km-200)*0.45 + 200)
    else:
        return"o valor da passagem é de: {0}".format(km*0.5)