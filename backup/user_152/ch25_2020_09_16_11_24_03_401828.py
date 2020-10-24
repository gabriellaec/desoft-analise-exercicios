import math
def acerto_de_jaca (velocidade, angulo):
    g = 9.8
    d = (velocidade**2 *math.sin(angulo))/g 
    if ((100 - d)>2):
        print("Muito longe")
    elif ((100 - d)<2):
        print("Muito perto")
    else:
        print("Acertou!")
              
v = float(input("Entre com a velocidade: "))
a = float(input("Entre com o angulo: "))
acerto_de_jaca(v, a)                