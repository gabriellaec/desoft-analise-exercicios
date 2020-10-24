import json

custo = 0

with open('estoque.json', 'r') as arquivo_json:
    conteudo = arquivo_json.read()
    dic = json.loads(conteudo)['produtos']
    for prod in dic:
        quantidade = int(prod['quantidade'])
        valor = float(prod['valor'])
        custo += quantidade*valor

print(custo)
        