import json
with open('estoque.json','r') as arquivo:
    texto = arquivo.read()
dic = json.loads(texto)
produtos = dic['produtos']
valor = 0
for e in produtos:
    valor += (e['quantidade'] * e['valor'])
print(valor)