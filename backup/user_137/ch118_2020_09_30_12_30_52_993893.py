import math

def reflexao_total_interna(n1, n2, theta2):
    if n2 > n1 and (math.sin(math.radians(theta2)) > 0 or math.sin(math.radians(theta2)) < 0):
        return False
    else:
        return True