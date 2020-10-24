import math

def calcula_distancia_do_projetil(velocidade, angulo, altura):
	g = 9.8   
	a = (velocidade**2)/2*g
    b = 2*g*altura/(velocidade**2)*(math.sin(angulo)**2)
    distancia = a * (1 + math.sqrt(1 + b))*math.sin(2*angulo)
    return distancia