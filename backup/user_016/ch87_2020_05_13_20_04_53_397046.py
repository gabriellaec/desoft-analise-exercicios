with open('churras.txt','r') as arquivo:
    linhas = arquivo.readlines()
    total = []
    for linha in linhas:
        linha.split(',')
        quantidade = int(linha[1])
        preço = float(linha[2])
        total = quantidade*preço
print(sum(total))
        