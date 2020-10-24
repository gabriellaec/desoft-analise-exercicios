soma=0
with open('macacos-me-mordam.txt','r') as arquivo:
    x=arquivo.read()
    for i in x:
        y=i.lower()
        if y == 'banana':
            soma+=1
print(soma)
    