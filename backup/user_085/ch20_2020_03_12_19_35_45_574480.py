a = float(input('Digite a distancia que deseja percorrer: '))
if a<=200:
    a = a*0.50
    ff = '{:.2f}'.format(a)
    print(ff)
else:
    a = (200*0.50) + ((a-200)*0.45)
    ff = '{:.2f}'.format(a)
    print(ff)