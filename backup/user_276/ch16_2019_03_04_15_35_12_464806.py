def distancia_euclidiana(x1, y1, x2, y2):
	dist = ((x1 - x2)**2 + (y1 - y2)**2)**1/2
    return dist
a = distancia_euclidiana(1, 2, 3, 4)
print(a)