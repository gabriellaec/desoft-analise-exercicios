import math

def dist_proj(v,ang):
    return v**2*math.sin(2*ang)/9.8

v= float(input("Qual a velocidade da jaca? "))
ang=math.radians(float(input("Qual o ângulo da jaca? ")))

if dist_proj(v,ang) < 98:
    print("Muito perto")
elif dist_proj(v,ang) > 102:
    print("Muito longe")
else:
    print("Acertou!")