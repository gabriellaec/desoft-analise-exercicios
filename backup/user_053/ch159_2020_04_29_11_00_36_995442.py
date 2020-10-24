import json

# Carrega texto
with open('estoque', 'r') as arquivo_json:
    texto = arquivo_json.read()

# Converte para dicionário
dicionario = json.loads(texto)

# Calcula preço
preco = 0
for produto in dicionario:
    qtde = dicionario['quantidade']
    preco = dicionario['valor']
    preco += qtde*preco

print(preco)