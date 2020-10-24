import math
dif = []
for a in range(0, 91, 1):
    senb = (4*a*(180-a))/(49500 - a*(180-a)):
    senm = math.sin(a)
    dif.append(-(senb-senm))
    print(abs(dif))
    
    