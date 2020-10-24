with open ('churras.txt','r') as minitab:
    minitab = minitab.read()
    
lista = minitab.split('\n')
lista = ','.joint(lista)
lista = lista.split(',')
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