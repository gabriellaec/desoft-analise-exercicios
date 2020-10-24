with open("macacos-me-mordam.txt", "r") as arquivo:
    total=0
    conteudo=arquivo.read()
    lista=conteudo.split()
    for i in lista:
        if i=='Banana':
            total=total+1
    print(total)   
