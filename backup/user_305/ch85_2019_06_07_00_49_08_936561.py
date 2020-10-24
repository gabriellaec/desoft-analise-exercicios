with open ('macacos-me-mordam','r') as arquivo:
    conteudo = arquivo.read()
    separar = conteudo.split()
    i = 0
    for k in separar:
        if k == "banana":
            i+=1
print (i)