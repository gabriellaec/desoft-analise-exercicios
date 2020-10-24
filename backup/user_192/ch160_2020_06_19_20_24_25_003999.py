import math

x = 0
for x in range(0, 90):
    python = math.sin(x)
    bhaskara = (4*x*(180 - x))/(40500 - x*(180 - x))
    modulo = bhaskara - python
    if python != bhaskara:
        print(max(modulo))