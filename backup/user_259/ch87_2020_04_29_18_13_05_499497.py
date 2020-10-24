soma = 0
with open('churras.txt', 'r') as churras:
    conteudo = churras.readlines()
for linha in conteudo:
    linha = linha.split(',')
    quantidade = float(linha[1])
    valor = float(linha[2])
    soma+=quantidade*valor
print(soma)