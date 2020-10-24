import math

def snell_descartes(n1,n2,teta2):
    teta2Rad=math.radians(teta2)
    senteta1=(n2/n1)*math.sin(teta2Rad)
    return senteta1

def reflexao_total_interna(n1,n2,teta2):
    if n2>n1 and snell_descartes(n1,n2,teta2):
        return True
    else:
        return False