import json
with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)
    
    total = 0
    
    for p in estoque['produto']:
        total += p['quantidade'] * p['valor']
    print (total)