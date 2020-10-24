soma=0
with open('macacos-me-mordam.txt','r') as arquivo:
    x=arquivo.readline()
    y=x.lower()
    for i in y:
        if i == 'banana':
            soma+=1
print(soma)
    