matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = max(matriz[0])
b = max(matriz[1])
c = max(matriz[2])
def encontra_maximo(a, b ,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c

print(encontra_maximo(a, b ,c))