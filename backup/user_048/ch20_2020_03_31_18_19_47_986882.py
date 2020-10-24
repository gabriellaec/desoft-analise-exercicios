d=int(input("qual a distancia em km"))
if d<=200:
    y=0.5
else:
    y=0.45
p=d*y

print("%.2f" % p)