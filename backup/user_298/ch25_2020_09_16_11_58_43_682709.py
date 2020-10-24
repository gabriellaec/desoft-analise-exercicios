v = float(input("Qual e a velocidade? "))
θ = float(input("Qual o angulo? "))
import math
def jaca_war(v,θ):
    g = 9.8
    θ = math.radians(θ)
    a = (v**2)*math.sin(2*θ)
    d = a/g
    if 98 < d < 102:
        return "Acertou!"
    if d < 98:
        return "Muito perto"
    else:
        return "Muito longe"
print(jaca_war(v,θ))