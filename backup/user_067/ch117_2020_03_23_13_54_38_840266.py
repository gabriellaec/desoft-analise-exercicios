import math
def snell_descartes(n1, n2, teta1):
    teta1 = (teta1/180)*3.14
    sen_teta2 = n1*math.sin(teta1)/n2
    teta2 = math.asin(sen_teta2)*180/3.14
    return teta2