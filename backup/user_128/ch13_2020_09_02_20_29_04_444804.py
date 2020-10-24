import math
def encontra_cateto(cat, hipo):
    cat_dif = math.sqrt((((hipo)**2) -  ((cat)**2)))
    return cat_dif

resposta = encontra_cateto(3, 5)
print(resposta)