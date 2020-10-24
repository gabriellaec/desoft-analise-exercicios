with open("dados.csv", "r") as arquivo:
    conteudo=arquivo.read()
    novo=conteudo.replace(",", "\t")

        