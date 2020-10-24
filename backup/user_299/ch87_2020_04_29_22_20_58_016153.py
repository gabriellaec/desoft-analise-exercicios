with open ('churras.txt','r') as minitab:
    lista = minitab.split(',')
dicio = {}
for i in range(0,len(lista),3):
    nome = lista[i]
    q = lista[i+1]
    preco = lista[i+2]
    dicio[nome] = q*preco

soma = 0
for gasto in dicio.values():
    soma+=gasto

print(soma)