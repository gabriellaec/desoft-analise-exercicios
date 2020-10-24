d = float(input("Qual a distancia percorrida?"))
if d> 0 or d <= 200:
    print 10
elif d > 200:
    v = 10 + (d - 200)*0.45
print ("O valor cobrado será {0:.2f}".format(v))