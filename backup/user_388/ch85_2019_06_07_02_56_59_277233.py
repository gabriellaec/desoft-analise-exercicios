with open('macacos-me-mordam.txt', 'r') as f:
    arquivo = f.read()
soma = 0
x = arquivo.split(' ')
for i in x:
    if i.lower() == 'banana':
        soma+=1
        
print(soma)
        