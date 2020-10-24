import math
def eh_bissexto(ano):
    if math.remainder(ano,400) == 0:
        return True
    elif math.remainder(ano,100)==0:
        return False
    elif math.remainder(ano,4)==0:
        return True
    else:
        return False
    