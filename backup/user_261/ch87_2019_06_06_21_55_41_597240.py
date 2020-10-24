valor=0.00
with open ('churras.txt','r') as arquivo:
    a=arquivo.read()
    colunas=a.split(',')
    for valores in colunas:
        valor+=colunas[1]*colunas[2]
print(valor)
    