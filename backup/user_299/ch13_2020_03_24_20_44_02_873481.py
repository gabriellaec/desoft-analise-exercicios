import math

def encontra_cateto(a,c):
    b = math.sqrt(math.sqrt((a-c)*(a+c)*(a-c)*(a+c)))
    return b