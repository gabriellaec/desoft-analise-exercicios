import json
with open("estoque.json", "r2") as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)
    total = 0
    for p in estoque["produtos"]:
        total += p["quantidade"] * p["valor"]
    print(total)