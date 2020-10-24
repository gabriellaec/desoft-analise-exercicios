
x = float(input("distancia?"))
if x <= 200:
    print ( "{0:.2f}".format(x/2))
else:
    print( "{0:.2f}".format(100 + 0.45*(x-200)))


