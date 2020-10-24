from mat import sen
def snell_descartes (n1, n2, anguloI) :
    ânguloR = ( n1/n2 ) * sen(anguloI)
    return ânguloR

n1 = input ("qual o meio que o raio provem?")
n2 = input (" qual meio para o qual o raio passsa?")
anguloI = input ("qual o angulo de incidência?")

print (snell_descartes)