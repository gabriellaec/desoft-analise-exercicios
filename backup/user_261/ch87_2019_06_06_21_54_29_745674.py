valor=0.00
with open ('churras.txt','r') as arquivo:
    a=arquivo.read()
    colunas=a.split(',')
    for valores in coluna:
        valor+=coluna[2]*coluna[3]
print(valor)
    