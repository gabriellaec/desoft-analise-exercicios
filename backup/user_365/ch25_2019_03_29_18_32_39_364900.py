dist=int(input("qual é a distância que vc quer percorrer?"))

if dist <= 200 :
    valor=dist*0.50
    print(valor)
else:
    valor=dist*0.45
    print(valor)