distancia = int(input("Qual a distância que você quer percorrer? ")
if distancia <= 200:
                preco_da_passagem = distancia*0.5
else:
                preco_da_passagem = (distancia - 200)*0.45 + 200*0.5
print("Preço da passagem: R${0}".format(preco_da_passagem))
            