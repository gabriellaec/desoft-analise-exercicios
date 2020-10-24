import json 

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()

dic_produtos = json.loads(conteudo)
s = 0

for lista in dic_produtos.values():

    for dic in lista:
        valor = dic['valor']
        quantidade = dic['quantidade']
        s += valor*quantidade

print(s)