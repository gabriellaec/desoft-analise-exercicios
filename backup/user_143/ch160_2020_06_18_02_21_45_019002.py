import numpy as np
import math
x = np.arange(0, 91, 1)
dife = []
for i in x:
    senx = (4 * i * (180 - i)) / 40500 - i * (180 - x)
    k = math.sin(math.radians(i))
    dif = abs(senx - k)
    dife.append(dif)
a = max(dife)
print (a)