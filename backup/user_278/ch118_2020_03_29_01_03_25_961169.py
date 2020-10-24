def reflexao_total_interna(n1,n2,o2):
    import math
    x=n2*math.sin(math.radians(o2))/n1
    #x = seno de o1
    if x>1:
        return ("True")
    else:
        return ("False")
print (reflexao_total_interna(1,2,60))