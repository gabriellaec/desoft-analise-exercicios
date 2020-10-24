import math
def reflexao_total_interna(n1, n2, teta2):
    while reflexao_total_interna(n1, n2, teta2) > 1:
        return True
    else: 
        return False
