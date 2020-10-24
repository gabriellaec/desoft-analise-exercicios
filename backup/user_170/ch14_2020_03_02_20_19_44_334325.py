
import math
g = 9,8
def calcula_distancia_do_projetil(v,a,y0):

    d = v**2/2*g*(1+(1+(2*g*y0/v**2*(math.sin(a)**2)**(1/2)))*math.sin(2*a)
    return(d)

b = calcula_distancia_do_projetil(2,3,4)
print(b)