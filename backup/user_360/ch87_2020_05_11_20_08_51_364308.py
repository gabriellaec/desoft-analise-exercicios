with open('churras.txt', 'r') as chu:
    file = chu.readlines()
preco = 0
for i in file:
    item = i.split(',')
    preco += float(item[1])*float(item[2])
print(preco)
          