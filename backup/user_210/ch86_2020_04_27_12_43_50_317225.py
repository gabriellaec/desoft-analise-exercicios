with open("dados.csv", "r") as file:
    conteudo = file.read().split(",")
    print("\t".join(conteudo))