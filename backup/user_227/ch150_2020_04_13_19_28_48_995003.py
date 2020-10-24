import math
def calcula_pi(n):
    pi_quadrado=0
    denominador=1
    while denominador<=n:
        pi_quadrado+=6/(denominador**2)
        denominador+=1
    pi=math.sqrt(pi_quadrado)
    return pi