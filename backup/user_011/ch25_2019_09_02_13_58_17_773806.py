d = float(input("distancia? "))
if d <= 200:
    preço = d*0.5
    print( "R$ {0:.2f}".format(preço))
elif d > 200:
    preço1 = 100 + 0.45*(d - 200)
    print( "R$ {0:.2f}".format(preço1))
          