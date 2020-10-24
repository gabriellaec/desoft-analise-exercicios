custo = 0
with open("churras.txt", "r") as file:
    conteudo = file.read().split("\n")
    for each in conteudo:
        quantidade, preco = each.split(",")[1:]
        custo += float(quantidade)*float(preco)
