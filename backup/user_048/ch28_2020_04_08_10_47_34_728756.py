sumo=[]
o=0
for o in range(100):
    y=1/(2**o)
    sumo.append(y)
    o=o+1
print(sum(sumo))

suma=[]
i=0
while i<98:
    y=1/(2**i)
    suma.append(y)
    i=i+1
print(sum(suma))