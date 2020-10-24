with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo= arquivo.readlines()
    palavras= []
    for i in conteudo:
        separa= i.split(' ')
        palavras += separa
l= []
for i in palavras:
    separa2= i.strip()
    separa= separa2.lower()
    l.append(separa)
    
c= 0 #contador
for i in l:
    if i == 'banana':
        c += 1