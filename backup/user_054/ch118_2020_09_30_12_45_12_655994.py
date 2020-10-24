import math

def reflexao_total_interna (n1, n2, teta2):
    if n2>n1 and math.sin(math.radians(teta2)) == 0:
        return True
    elif math.sin(math.radians(teta2))*n1/n2 > 1:
        return False
    