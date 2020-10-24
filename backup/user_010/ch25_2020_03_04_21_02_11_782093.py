import math
vel = float (input("Qual a velocidade do lançamento?"))
ang = float (input("Qual o ângulo de lançamento?"))
def jaca(x,y):
    z = (x**2*math.sin (math.radians (2*y)))/9.8
    return z
funcao = jaca (vel,ang)
if funcao >=98 and funcao<=102:
    print ("Acertou!")
elif funcao <98:
    print ("Muito perto")
else:
    print("Muito longe")
print (funcao)