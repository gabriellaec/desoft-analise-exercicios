with open("dados.csv", "a") as arquivo:
    conteudo=arquivo.read()
    novo=conteudo.replace(",", "	")

with open('dados.tsv', 'w') as arquivo:
    arquivo.write(novo)