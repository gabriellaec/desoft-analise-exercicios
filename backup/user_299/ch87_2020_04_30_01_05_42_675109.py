with open ('churras.txt','r') as minitab:
    minitab = minitab.read()
    
lista = minitab.split('\n')

nome = []
quantidade = []
preco = []

for e in lista:
    nomes, quantidades, precos = e.split(',')
    nome.append(nomes)
    quantidade.append(quantidades)
    preco.append(precos)

soma = 0
for i,n in enumerate(quantidade):
    n = float(n)
    p = float(preco[i])
    gasto = n*p
    soma+=gasto

print(soma)