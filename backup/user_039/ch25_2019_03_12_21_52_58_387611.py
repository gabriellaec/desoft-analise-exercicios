d=int(input('Qual a distancia que voce deseja percorrer?'))
if d<=200:
    print("{0:.2f}".format(0.50*d))
else:
    print("{0:.2f}".format(100+0.45*(d-200)))
    





