with open('churras.txt','r') as arquivo:
    linhas = arquivo.readlines()
    preço = []
    for linha in linhas:
        linha.split(',')
        preço.append(linha[1]*linha[2])
print(sum(preço))
        