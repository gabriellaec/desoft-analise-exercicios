import json
with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()
dicionario = json.loads(texto)
lista = []
for i in dicionario:
    for a in i:
        lista.append(a)
