with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

custo = 0    
for linha in linhas:
    lista = linha.split()
    custo += float(lista[-1])*float(lista[-2])

print(custo)