with open('churras.txt','r') as arquivo:
    leitura = arquivo.readlines()
soma,preco = 0,0    
for i in leitura:
    item = i.split(',')
    preco += float(item[1])*float(item[2])
print(preco)
    