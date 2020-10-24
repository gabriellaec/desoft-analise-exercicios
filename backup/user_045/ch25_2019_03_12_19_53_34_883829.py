km=float(input('distancia?'))
    if km>200:
        d=100 + km*0.45
    else:
        d=km*0.50
print('{:.2f}'.format(d))