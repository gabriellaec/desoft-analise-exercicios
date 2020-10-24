import math
def snell_descartes(n1, n2, teta1):
    sen_teta2 = n1*math.sen(teta1)/n2
    teta2 = arcsen(sen_teta2)
    return teta2