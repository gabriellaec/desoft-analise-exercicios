import math as mt
def reflexao_total_interna(n1, n2, O2):
    a=O2*mt.pi/180
    O1=180*(mt.asin(mt.sin(a)*n2/n1))/mt.pi
    if O1 > 90:
        print(O1)
        return True
    else:
        print(O1)
        return False