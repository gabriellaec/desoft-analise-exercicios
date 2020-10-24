with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo=arquivo.read()
    lista=conteudo.split()
    total=0
    for i in lista:
        if i.lower()=="banana":
            total+=1
print(total)
        