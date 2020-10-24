import json

# Carrega texto
with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()

# Converte para dicionário
dicionario = json.loads(texto)

# Calcula preço
custo = 0
produtos = dicionario['produtos']
for produto in produtos:
    qtde = produto['quantidade']
    valor = produto['valor']
    custo += qtde*valor

print(custo)