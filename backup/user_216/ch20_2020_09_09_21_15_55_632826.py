d = float(input("Distancia em km"))

if d <= 200:
    c = (0.5 * d)
else:
    c = (0.5*200 + (d-200)*0.45)


print("{0:.2f}".format(c))