import json

custo = 0

with open('estoque.json', 'r') as arquivo_json:
    conteudo = arquivo_json.read()
    dic = json.loads(conteudo)
    for prod in dic:
        quantidade = int(prod)
        valor = float(prod)
        custo += quantidade*valor

print(custo)
        