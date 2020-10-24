import numpy as np
import math
angulos = np.arange(0,91)
error = []
for a in angulos:
    bhaskara = 4*a*(180-a)/40500 - a*(180-a)
    r = math.radians(a)
    py = math.sin(r)
    result = abs(bhaskara-py)
    error.append(result)
print(max(error))
