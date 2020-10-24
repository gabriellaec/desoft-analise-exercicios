    import math
def reflexao_total_interna(n1,n2,O2):
    a = math.radians(O2)
    b = math.sin(a)
    c = n2/n1*b
    if c > 1:
        return True
    else:
        return False