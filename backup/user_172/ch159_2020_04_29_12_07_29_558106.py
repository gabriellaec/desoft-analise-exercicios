import json
with open ('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)
soma = 0
for x in dicionario.values():
    for y in x.values():
        a = y[1]
        b = y[2]
        soma = soma + a*b
print (soma)
        
        