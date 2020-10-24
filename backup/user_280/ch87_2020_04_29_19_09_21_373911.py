with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    lista_linhas = linhas.split()
    
custo = 0    
for linha in lista_linhas:
    lista_produtos = linha.split()
    custo += float(lista_produtos[-1])*float(lista_produtos[-2])

print(custo)