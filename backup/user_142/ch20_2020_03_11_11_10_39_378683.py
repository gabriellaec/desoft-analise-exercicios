D = float(input('qual a distancia percorrida?:'))
P1 = D*0.50
P2 = (D-200)*0.45
if D<=200:
    print ("{0:.2f}".format(P1))
else:
    print ("{0:.2f}".format(P2+P1))


   
        