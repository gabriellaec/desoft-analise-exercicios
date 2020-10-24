valor=0.00
with open ('churras.txt','r') as arquivo:
    a=arquivo.read()
    colunas=a.split(',')
    for valores in colunas:
        valor+=coluna[1]*coluna[2]
print(valor)
    