distancia = int(input("Qual a distância da sua viagem ?"))

if distancia < 200 or distancia == 200:                
    preco = distancia*0.50

elif distancia > 200:
    preco = 200 *0.50
    extra = distancia-200
    preco = preco + (extra*0.45)

final = round(preco, 2)
                
print(final)