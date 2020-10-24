d=float(input("Qual a distancia da viagem? "))
def preço_da_passagem(d):
    if d<=200:
        preco=d*0.5
        return preco
    elif d>200:
        preco=((d-(200-d))*0.5)+(d-200)*0.45
        return preco
print("O preço é {0:.2f}".format(preço_da_passagem(d)))