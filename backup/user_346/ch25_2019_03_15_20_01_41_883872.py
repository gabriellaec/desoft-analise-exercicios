distancia=float(input())
if distancia<=200.00:
    print("{0:.2}".format(distancia*0.5))
else:
    print("{0:.2}".format(100+(distancia-200)*0.45))