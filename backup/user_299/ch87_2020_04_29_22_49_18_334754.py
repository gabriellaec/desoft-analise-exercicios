minitab = 'Carvão,2,9.90,Refrigerante,3,8.35,Picanha,2,69.80,Linguiça,2,15.98,Coxinha da Asa,2,12.39,Contra Filé,3,25.98'
lista = minitab.split(',')
dicio = {}
for i in range(0,len(lista),3):
    nome = lista[i]
    q = float(lista[i+1])
    preco = float(lista[i+2])
    valor = q*preco
    dicio[nome] = valor

soma = 0
for gasto in dicio.values():
    soma+=gasto

print(soma)