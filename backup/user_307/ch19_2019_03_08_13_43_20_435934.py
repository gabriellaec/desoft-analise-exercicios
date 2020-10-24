#Faça uma função que calcule a distância alcançada por um projétil lançado com velocidade v em um ângulo θ 
#de uma altura y0. A distância é dada pela fórmula
import math
def calcula_distancia_do_projetil(v,teta,y0):
    g=9.8
    y=((v**2)/2*g)*(1+math.sqrt(1+(2*g*y0)/((v**2)*(math.sin(teta))**2)))*math.sin(2*teta)
    return y