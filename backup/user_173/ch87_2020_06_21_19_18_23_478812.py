with open('churras.txt','r') as arquivo:
    leitura = arquivo.readlines()
soma,preco = 0,0    
for i in leitura:
    item = i.split(',')
    preco += (item[1])*(item[2])
print(preco)
    