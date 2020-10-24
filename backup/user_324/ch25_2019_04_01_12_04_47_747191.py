d=int(input("Qual a distancia desejada: "))
if d<=200:
    v=d*0.5
elif d>200:
    v=d*0.5+(d-200)*0.45
print(format(v,'.2f'))
      