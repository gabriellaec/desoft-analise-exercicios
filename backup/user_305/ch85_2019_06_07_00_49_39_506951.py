with open ('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    conteudo = arquivo.lower()
    separar = conteudo.split()
    i = 0
    for k in separar:
        if k == "banana":
            i+=1
print (i)