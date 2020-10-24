d = int(input("Quantos km você pretende percorrer? "))
if d<=200:
    y = 0.5*d
    print("R${0:.2f}".format(y))
elif d>200:
    x=200*.5
    y = 0.45*(d-200)
    z=x+y
    print("R${0:.2f}".format(z))