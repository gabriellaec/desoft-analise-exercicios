import math

a = float(input ("Digite a velocidade do lançamento: "))
b = float(input ("Digite o ângulo em graus do lançamento: "))

def distância(v,teta):
    d = (v**2 * math.sin(2*teta))/9.8
    return d

if 98 <= distância(a,math.radians(b)) <= 102:
    print ("Acertou!")

if distância(a,math.radians(b)) > 102:
    print ("Muito longe")
    
if distância(a,math.radians(b)) < 98:
    print ("Muito perto")