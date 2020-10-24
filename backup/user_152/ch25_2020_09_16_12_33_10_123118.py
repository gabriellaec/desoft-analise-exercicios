import math
def acerto_de_jaca (velocidade, angulo):
    g = 9.8
    d = (velocidade**2 *math.sin(math.radians(2*angulo)))/g 
    if (d>=98 and d<=102):
        return "Acertou!"
    elif (d<98):
        return "Muito perto"
    else:
        return "Muito longe!"
              
v = float(input("Entre com a velocidade: "))
a = float(input("Entre com o angulo: "))
print(acerto_de_jaca(v, a))                