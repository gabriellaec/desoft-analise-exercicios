d = float(input("Distancia: "))

if d < 200:
    p = d * 0.5

else:
    p = (d - 200) * 0.45 + 100

print("{0:.2f}".format(p))
