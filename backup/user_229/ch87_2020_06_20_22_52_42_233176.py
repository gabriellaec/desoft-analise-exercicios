with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    
i = 0
qtd = 0
preço = 0
while i <= (len(lista) - 1):
    i += 1
    qtd = int(lista[i])
    i += 1
    preço += qtd*float(lista[i])
    i += 1
    
print(preço)