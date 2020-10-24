dist=float(input("qual a distancia em km?"))
if dist < 200:
    a=dist*0.5
    print('{:.2f}'.format(a))
else:
    b=(200*0.5+(dist-200)*0.45)
    print('{:.2f}'.format(b))
