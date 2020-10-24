def distancia_euclidiana(x1, x2, y1, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d
m = 2;
n = 2;
p = 1;
q = 1;
e = distancia_euclidiana(m, n, p, q);
print('A distância entre esses dois pontos (x1, y1) e (x2, y2) é de {0}'. format(e));