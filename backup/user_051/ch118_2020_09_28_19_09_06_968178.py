import math as mt
def reflexao_total_interna(n1, n2, O2):
    a=mt.radians(O2)
    O1=mt.sin(a)*n2/n1
    print (O1)
    if O1 > 1:
        return True
    else:
        return False
n1=1
n2=2
O2=150
q=reflexao_total_interna(n1, n2, O2)
print(q)