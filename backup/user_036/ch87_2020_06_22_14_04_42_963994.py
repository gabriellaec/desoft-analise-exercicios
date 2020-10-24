with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
preco = 0
s = 0
for i in conteudo:
    item = i.split()
    s+= float(item[1])*float(item[2])
print(s)