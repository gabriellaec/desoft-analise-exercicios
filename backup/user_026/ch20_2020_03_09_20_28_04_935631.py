def preco_da_viagem(distancia):
    if distancia <= 200:
        return "O preço da sua viagem é R${0:.2f}".format(distancia*0.5)
    else:
        return "O preço da sua viagem é R${0:.2f}".format(100+((distancia-200)*0.45))

distancia= int(input("Qual a distancia a percorrer desejada (em km)? "))

print(preco_da_viagem(distancia))