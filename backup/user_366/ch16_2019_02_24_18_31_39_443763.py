def distancia_euclidiana(x1, y1, x2, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return d
m = 5;
n = 10;
p = 1;
q = 5;
e = distancia_euclidiana(m, n, p, q);
print(e);