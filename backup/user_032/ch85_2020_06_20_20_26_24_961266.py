with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.readlines()
contador = 0
for texto in conteudo:
    z = texto.strip()
    x = z.split(" ")
    for p in x:
        palavra = p.lower()
        if palavra == 'banana':
            contador += 1
print(contador)