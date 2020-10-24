def preco_da_viagem(distancia):
    if distancia<=200:
        return "O preço da sua viagem é R${0:.2f}".format(distancia*0.5)
    else:
        return "O preço da sua viagem é R${0:.2f}".format(distancia*0.5)+((distancia-200)*0.45)

distancia = int (input("Qual a distância a percorrer desejada?= km"))  