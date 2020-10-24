d = float(input("Qual a distancia percorrida?"))
if  d < 200:
    v = 0.5*d
elif d >= 200:
    v = (0.5*d) + ((d - 200)*0.45)
print ("O valor cobrado será {0:.2f}".format(v))