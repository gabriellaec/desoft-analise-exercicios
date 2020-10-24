with open("churras.txt", "r") as file:
    conteudo = file.read().split(",")
    quantidade = conteudo[::2]
    preco = conteudo[::3]
    print(quantidade,preco)
