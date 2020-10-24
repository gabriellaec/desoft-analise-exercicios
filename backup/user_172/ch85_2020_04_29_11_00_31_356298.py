with open ('macacos-me-mordam', 'r') as arquivo:
    conteudo = arquivo.read()
lista=[]
x = conteudo.split()
i = 0
while i < len(x):
    if x[i] == 'banana' or x[i] == 'Banana' or x[i] == 'BANANA' or x[i] == 'BaNaNa':
        lista.append(x[i])
    i+=1
    
print (len(lista))
