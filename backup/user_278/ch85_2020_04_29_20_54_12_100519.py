with open ("macacos-me-mordam.txt","r") as arquivo:
    conteudo = arquivo.read()
    frasE = conteudo.split()
    frase = frasE.lower()
    oc = 0
    for i in frase:
        if frase[i]=="banana":
            contador += 1
print (contador)