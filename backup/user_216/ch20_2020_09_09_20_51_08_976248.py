d = int(input("Distancia em km"))

if d <= 200:
    print(0.5 * d)
else:
    print(0.5*200 + (d-200)*0.45)