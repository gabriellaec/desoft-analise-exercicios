with open('churras.txt','r') as arquivo:
    linhas = arquivo.readlines()
    total = []
for linha in linhas:
    linha.split(',')
    total = float(linha[1])*float(linha[2])
    total = quantidade*preço
print(sum(total))
        