v=int(input("Qual a velocidade de lançamento da jaca?"))
teta=float(input("Qual o ângulo de lançamento da jaca?"))
g=9.8
distancia=(v**2*math.sin(2*teta))/g    
if distancia==100:
    print("Acertou!")
elif distancia<100:
    print("Muito perto")
else:
    print("Muito longe")