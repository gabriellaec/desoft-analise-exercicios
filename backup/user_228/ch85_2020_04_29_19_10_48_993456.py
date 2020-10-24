with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo=arquivo.read()
    total=0
    for i in conteudo:
        if i=="banana" or i=="Banana":
            total+=1
print(total)
        