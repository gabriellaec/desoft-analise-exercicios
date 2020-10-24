km=float(input('distancia: '))
if km<=200:
    y=km*0.5
    print('{0:.2f}'.format(y))
elif km>200:
    y=(200*0.5)+(km-200)*0.45
    print('{0:.2f}'.format(y))
 