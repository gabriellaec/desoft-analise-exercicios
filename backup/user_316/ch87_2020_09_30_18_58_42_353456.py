price = 0

with open('churras.txt', 'r') as file:
    content = file.readlines()    

for e in content:
    dados = e.split(',')
    price += float(dados[1]) * float(dados[2])
    
print(price)