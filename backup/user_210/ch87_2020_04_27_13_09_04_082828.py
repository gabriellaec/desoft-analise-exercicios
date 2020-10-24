custo = 0
with open("churras.txt", "r") as file:
    conteudo = file.read().split("\n")[:-1]
    for each in conteudo:
        quantidade, preco = each.split(",")[1:]
        custo += float(quantidade)*float(preco)

print(custo)
