import json 

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()

dic_produtos = json.loads(conteudo)
s = 0

for produto in dic_produtos:

    for mercadoria in dic_produtos[produto]:
        valor = dic_produtos[produto]['valor']
        quantidade = dic_produtos[produto['quantidade']]
        s += valor*quantidade

print(s)