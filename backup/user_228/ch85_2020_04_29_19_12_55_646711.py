with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo=arquivo.read()
    lista=conteudo.split()
    total=0
    for i in lista:
        if i=="banana" or i=="Banana" or i=="BANANA":
            total+=1
print(total)
        