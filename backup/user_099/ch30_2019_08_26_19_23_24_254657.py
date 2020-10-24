from math import sin, pi

def catapulta(v,teta):
    return v**2*sin(2*teta)/9.8

v=float(input("Qual a velocidade, em m/s?"))
teta=float(input("Qual o ângulo, em graus?"))
teta=teta*2*pi/360

if catapulta(v,teta)==100:
    print("Acertou!")
elif catapulta(v,teta)>100:
    print("Muito longe")
else:
    print("Muito perto")