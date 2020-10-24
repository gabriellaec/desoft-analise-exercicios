d = int(input("Qual a distancia da viagem: "))
k=0
if d<=200:
    k = 0.5*d
    print(k)
elif d>200:
    k = d*0.5+(d-200)*0.45
    print(k)