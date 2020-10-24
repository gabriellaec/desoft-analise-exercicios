import math
def eh_bissexto(ano):
    if math.remainder(ano,4) == 0 and math.remainder(ano,100) != 0:
        return "True"
    else:
        return "False"
    