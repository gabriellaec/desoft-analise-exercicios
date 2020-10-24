import json 

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()

dic_produtos = json.loads(conteudo)
s = 0

for produto in dic_produtos:

    for dic_mercadorias in produto:
        valor = dic_mercadorias['valor']
        quantidade = dic_mercadorias['quantidade']
        s += valor*quantidade

print(s)