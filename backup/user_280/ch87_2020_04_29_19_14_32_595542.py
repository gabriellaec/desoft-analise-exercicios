with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    lista_linhas = linhas.split()

custo = 0
for linha in lista_linhas:
    produto = linha.split()
    custo += float(produto[-1])*float(produto[-2])
print(custo)