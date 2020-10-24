d = input("Quantos km você pretende percorrer? ")
if d<=200:
    y = 0.5*d
    print("R${0:.2f}".format(y))
elif d>200:
    y = 0.45*d
    print("R${0:.2f}".format(y))