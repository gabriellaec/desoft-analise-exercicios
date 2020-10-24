import math

l = []
l1 = []
for i in range(91):
    l.append((4 * i * (180-1)) / (40500 - i * (180 - i)))
    l1.append(math.sin(math.radians(i)))
y = 0
for x in range(len(l)):
    if y < abs(l[x]-l1[x]):
        x+=1
        y = abs(l[x]-l1[x])
        x+=1
    else:
        x+=1
print(y)