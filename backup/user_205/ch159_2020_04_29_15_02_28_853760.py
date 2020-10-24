import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

custo_total = 0
for lista in dicionario.values():
    for dic in lista: 
            custo = dic['quantidade']*dic['valor']
            custo_total+=custo
print (custo_total)
            