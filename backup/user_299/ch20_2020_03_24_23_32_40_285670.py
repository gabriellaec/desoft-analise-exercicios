d = float(input("Qual a distância em km que você deseja percorrer?"))
if d<=200:
    p = 0.5*d
    print("O valor a ser pago é {0:.2f}".format(p))
else:
    p = 0.5*d+0.45*(d-200)
    print("O valor a ser pago é {0:.2f}".format(p))