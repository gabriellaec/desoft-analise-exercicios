distancia=float(input())
if distancia<=200.00:
    print("{0:.2f}".format(distancia*0.5))
else:
    print("{0:.2f}".format(100+(distancia-200)*0.45))