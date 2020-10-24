with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    listas = linhas.split()

custo = 0    
for lista in listas:
    custo += float(lista[-1])*float(lista[-2])

print(custo)