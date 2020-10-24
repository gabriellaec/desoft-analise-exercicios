with open('macacos-me-mordam.txt','r') as arquivo:
    texto = arquivo.read()

    
tx = texto.split()
x = 0
for i in tx:
    i.lower()
    if i == 'banana':
        x+=1
print(x)