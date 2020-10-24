improt json
with open('estoque.json', 'r') as arquivo:
    read = arquivo.read()
dicionario = json.loads(read)
resultado = 0
for i in dicionario['produtos']:
    preco = i['quantidade'] * i['valor']
    resultado += preco
print (resultado)