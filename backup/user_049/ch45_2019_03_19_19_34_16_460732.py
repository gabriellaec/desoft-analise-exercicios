zera_negativos=[]
print(zera_negativos)
i = 0
while i < len(zera_negativos):
    if zera_negativos[i] < 0:
        zera_negativos[i] = 0
    i += 1
print(zera_negativos)