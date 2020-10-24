with open ( 'macacos-me-mordam.txt' , 'r' ) as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.lower()
    cont_splitado = conteudo.split()
i = 0
for k in cont_splitado:
    if k  == 'banana':
        i+=1
print(i)