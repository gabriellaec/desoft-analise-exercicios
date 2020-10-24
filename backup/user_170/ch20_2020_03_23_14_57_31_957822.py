d = float(input('Qual distancia percorrera?: '))
if d <= 200:
    p = d*0.5
    print(round(p ,2))
else:
    p = (200*0.5)+((d-200)*0.45)
    print(round(p,2))

