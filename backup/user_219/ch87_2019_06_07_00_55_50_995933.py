with open('churras.txt') as arquivo:
    preco=0
    for linha in arquivo:
        linha= linha.split(',')
        linha[1]= int(linha[1])
        linha[2]= float(linha[2])
        preco+= linha[1]*linha[2]
    print(preco)