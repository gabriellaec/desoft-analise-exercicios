import json

with open ('estoque.json', 'r') as arquivo_json:
    conteudo = arquivo_json.read()

# Criando um dicionário no python a partir do texto
dicionario = json.loads(conteudo)

# dicionario['produtos'] é uma lista de dicionários
# Verifica cada dicionário da lista
valor_total = 0
for dicio in dicionario["produtos"]:
    qtde = dicio["quantidade"]
    preco = dicio["valor"]
    valor_total += qtde*preco

print(valor_total)