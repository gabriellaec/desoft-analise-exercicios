with open("churras.txt",'r') as arquivo:
    price = 0
    for linha in arquivo:
        linha = linha.split(",")
        linha[1] = int(linha[1])
        linha[2] = float(linha[2])
        price += linha[1]*linha[2]
    print(price)