with open('macacos-me-mordam.txt','r') as arquivo:
    texto = arquivo.read()

x = 0
for i in texto:
    i.lower()
    if i == 'banana':
        x+=1
print(x)