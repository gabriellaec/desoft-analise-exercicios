import math

graus = range(0, 91)

diferenca = []
for a in graus:
    bhaskara = (4 * a * (180 - a)) / (40500 - a * (180 - a))
    python = math.sin(math.radians(a))
    diferenca.append(abs(bhaskara - python))

maximo = max(diferenca)
print(diferenca.index(maximo))