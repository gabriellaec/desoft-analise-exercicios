with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    lista_linhas = linhas.split()
    
lista_produtos = []
custo = 0
i = 0
while i < len(lista_linhas):
    lista_produtos.append(lista_linhas[i].split())
    i+=1

for produto in lista_produtos:
    custo += float(produto[-1])*float(produto[-2])
print(custo)