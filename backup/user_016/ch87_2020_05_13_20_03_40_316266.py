with open('churras.txt','r') as arquivo:
    linhas = arquivo.readlines()
    preço = []
    for linha in linhas:
        linha.split(',')
        preço.append(int(linha[1])*float(linha[2]))
print(sum(preço))
        