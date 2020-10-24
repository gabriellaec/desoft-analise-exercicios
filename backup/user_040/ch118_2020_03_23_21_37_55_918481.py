import math
def reflexao_total_interna(n1,n2,teta2):
    if n2*math.sin(math.radians(teta2))/n1 > 1:
        return True
        print ("Ocorreu reflexão")
    else:
        return False
        print ("Ocorreu refração")