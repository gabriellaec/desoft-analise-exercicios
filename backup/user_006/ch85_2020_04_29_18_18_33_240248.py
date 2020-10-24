with open("macacos-me-mordam.txt", "r") as arquivo:
    total=0
    conteudo=arquivo.read()
    lista=conteudo.split()
    jeitos=["Banana", "banana", "BaNaNa", "BANANA"]
    for i in lista:
        if i in jeitos:
            total=total+1
    print(total)   
