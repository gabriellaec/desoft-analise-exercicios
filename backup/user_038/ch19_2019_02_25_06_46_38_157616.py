import math
def calcula_distancia_do_projeto(velocidade, angulo, altura, gravidade):
    distancia = velocidade**2/(2*gravidade)*(1 + (1 + 2*gravidade*altura/velocidade**
                              2*math.sin(angulo)**2)**(1/2))*math.sin(2*angulo)
    print("A distancia percorrida pelo projétil é: {0}".format(distancia))
v = float(input("Informe a velocidade do projétil: "))
teta = float(input("Informe o angulo de lançamento do projétil: "))
h = float(input("Infomre a altura de lançamento do projétil: "))
g = float(input("Informe a gravidade: "))
calcula_distancia_do_projeto(v, teta, h, g)