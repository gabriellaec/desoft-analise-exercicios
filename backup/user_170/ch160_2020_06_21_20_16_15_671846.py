import math
error = []
for a in range(0,91):
    bhaskara = 4*a*(180-a)/40500 - a*(180-a)
    r = math.radians(a)
    py = math.sin(r)
    result = abs(bhaskara-py)
    error.append(result)
print(max(error))