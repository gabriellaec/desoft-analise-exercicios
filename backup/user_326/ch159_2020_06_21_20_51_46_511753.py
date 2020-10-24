import json

vlr_total = 0

with open('estoque.json', 'r') as leitura:
    conteudo = leitura.read()
    dicionario = json.loads(conteudo)
    for produto in dicionario['produtos']:
        quantidade = produto['quantidade']
        valor = produto['valor']
        vlr_total += quantidade * valor
print(vlr_total)
