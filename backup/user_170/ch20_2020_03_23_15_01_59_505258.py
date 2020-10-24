d = float(input('Qual distancia percorrera?: '))
if d <= 200:
    p = d*0.5
    print('{:.2f}'.format(p))
else:
    p = (200*0.5)+((d-200)*0.45)
    print('{:.2f}'.format(p))