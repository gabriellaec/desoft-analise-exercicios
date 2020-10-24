with open ('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    m = conteudo.lower()
    s = m.split()
cont = 0
for e in s:
    if e == 'banana':
        cont += 1


print(cont)