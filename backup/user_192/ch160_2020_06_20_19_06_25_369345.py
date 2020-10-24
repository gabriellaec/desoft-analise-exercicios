import math

x = 0
j = 0
d = 0
while 0 <= x <= 89:
    python = math.sin(x)
    bhaskara = (4*x*(180 - x))/(40500 - x*(180 - x))
    if abs(python - bhaskara) > d:
        d = abs(python - bhaskara)
        j = x
    x += 1
print(j)