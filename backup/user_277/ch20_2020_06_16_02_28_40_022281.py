d = int(input("Qual a distancia da viagem: "))
k=0
h=0
if d<=200:
    k = 0.5*d
if d>200:
    h = 0.45*d
total = h+k
print(total)