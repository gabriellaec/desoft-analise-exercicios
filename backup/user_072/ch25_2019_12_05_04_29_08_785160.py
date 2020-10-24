s = float(input('qual a distancia a percorrer ? '))
if s < 200:
    print('{0:.2f}'.format(s*0.5))
else:
    print('{0:.2f}'.format((s-200)*0.45 + 200*0.5))