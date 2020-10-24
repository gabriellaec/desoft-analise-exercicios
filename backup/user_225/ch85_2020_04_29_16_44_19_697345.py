with open("macacos-me-mordam.txt") as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split(" ")
    i = 0
    while i < len(lista):
        if "Banana" or "BANANA" or "BaNaNa" in lista:
            i+=1
    print (i)