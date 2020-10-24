import math as mt
def reflexao_total_interna(n1, n2, O2):
    a=mt.radians(O2)
    O1=mt.degrees(mt.asin(mt.sin(a)*n2/n1))
    if O1 > 90:
        print(O1)
        return True
    else:
        print(O1)
        return False