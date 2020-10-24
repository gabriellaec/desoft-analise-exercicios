d = float(input('distancia em km: '))
if d<=200:
    a = d*0.5
else:
    a = 100+(d-200)*0.45
print(a) 