with open ("macacos-me-mordam.txt","r") as arquivo:
    conteudo = arquivo.read()
    frasE = conteudo.lower()
    frase = frasE.split()
    oc = 0
    for i in range(0,len(frase)):
        if frase[i]=="banana":
            oc += 1
print (oc)