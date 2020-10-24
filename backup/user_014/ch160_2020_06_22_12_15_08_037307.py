from math import *

maior = 0
x = 0

while x <= 90:
    seno_python = sin(x)
    seno_formula = 4 * x * (180 - x)/40500 - x * (180 - x)
    diferenca = abs(seno_formula) - abs(seno_python)
    if diferenca > maior:
        maior = diferenca
    x += 1

print(maior)