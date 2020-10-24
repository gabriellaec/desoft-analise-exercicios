
d = int(input("Quantos km de viagem? "))
def Distancia(x):
    if x < 200:
        y = 0.5*x
        return y
    else:
        w = 0.5*x + 0.45*(x-200)
        return w
print(Distancia(d))
    