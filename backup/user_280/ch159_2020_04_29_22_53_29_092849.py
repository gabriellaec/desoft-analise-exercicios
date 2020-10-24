import json
with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()

dicionario = json.loads(texto)
produtos = dicionario["produtos"]

custo = 0
for produto in produtos:
    custo += produto['quantidade']*produto['valor']

print(custo)