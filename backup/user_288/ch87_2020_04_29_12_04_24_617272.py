import json

with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    churras = json.loads(conteudo)
    
    total = 0
    
    for p in churras[0]:
        total += p[1] * p[2]
    print (total)