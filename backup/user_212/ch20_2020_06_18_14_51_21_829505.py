distancia = int(input("Qual a distância da sua viagem ?")

preco = distancia*0.50

if distancia > 200:
    extra = distancia-200
    preco = preco + (extra*0.45)

final = round(preco, 2)
                
print(final)