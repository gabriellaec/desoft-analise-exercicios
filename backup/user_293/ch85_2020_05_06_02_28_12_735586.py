with open('macacos-me-mordam.txt','r') as arquivo:
    i = 0
    conteudo = arquivo.readlines()
    for e in conteudo:
        conteudo_lower = e.lower()
        conteudo_final = conteudo_lower.split()
        for a in conteudo_final:
            if a == "banana":
                i +=1
print(i)