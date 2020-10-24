with open("churras.txt",'r') as arquivo:
    price = 0
    for linha in arquivo:
        linha = linha.split(",")
        price += int(linha[1])*float(linha[2])
    print(price)