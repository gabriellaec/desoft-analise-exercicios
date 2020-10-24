import json
with open('estoque.json', 'r') as arquivo_json:
    conteudo = arquivo_json.read()
    estoque = json.loads(conteudo)
    total = 0
    for p in estoque["produtos"]:
        total += p["quatidade"] * p["valor"]
    print(total)