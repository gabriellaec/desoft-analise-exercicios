d=int(input("Qual é a distância de sua viagem ?"))
if(d<=200):
    p=d*0.50
else:
    p=((d-200)*0.45)+100
print("{0:.2f}".format(p))