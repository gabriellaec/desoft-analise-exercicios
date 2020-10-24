with open("macacos-me-mordam.txt","r") as arquivo:
    ler = arquivo.read()
    lista = ler.split()
    conta_banana = 0
    for i in lista:
        if i.lower() == "banana":
            conta_banana += 1
    print(conta_banana)
            