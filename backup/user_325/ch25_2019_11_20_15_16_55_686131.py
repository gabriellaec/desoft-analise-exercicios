dist = float(input("Distancia"))
p = 0
if dist <= 200:
    p = 0.5 * dist
else:
    p = 100 + 0.45 * dist