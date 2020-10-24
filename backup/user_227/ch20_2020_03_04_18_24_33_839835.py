distancia = float(input("Qual a distância que você quer percorrer? "))
if distancia <= 200:
    print(distancia*0.5)
else:
    print((distancia - 200)*0.45 + 100) 