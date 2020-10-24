v = float(input("velocidade da jaca (m/s): "))
theta = float(input("angulo de lancamento da jaca(graus): "))
g = 9.8
d = (v**2*np.sin(np.radians(2*theta)))/g
if 98<= d <=102:
    print ("Acertou!")
elif d < 98:
    print ("Muito perto")
else:
    print ("Muito longe")