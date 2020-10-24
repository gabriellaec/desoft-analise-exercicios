import json

with open('estoque.json', 'r') as estoque:
    conteudo = estoque.read()
    
dicionario = json.loads(conteudo)
    
for nome, produtos in dicionario.items():
    custo_total = 0
    for i in produtos:
        qtd = 0
        for info, value in i.items():
            if info == 'quantidade':
                qtd += value
            elif info == 'valor':
                custo_total += qtd*value
            
print(custo_total)