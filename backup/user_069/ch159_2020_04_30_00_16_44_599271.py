import json
with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    dic = json.loads(conteudo)
    total = 0
    for p in dic['produtos']:
        total += p['quantidade']*p['valor']
print(total)