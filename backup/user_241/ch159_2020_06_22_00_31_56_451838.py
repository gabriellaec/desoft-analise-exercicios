import json

arquivo = open('estoque.json','r')
string = arquivo.read()
arquivo.close()
dicionario = json.loads(string)
produtos = dicionario['produtos']
soma = 0
for produto in produtos:
    quantidade = produto['quantidade']
    valor = produto['valor']
    soma += quantidade * valor 
print(soma)