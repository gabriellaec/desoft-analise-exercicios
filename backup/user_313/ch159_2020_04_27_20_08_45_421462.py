import json

with open('estoque.json', 'r')as arquivo_json:
    texto = arquivo_json.read()
    
dicionario = json.loads(texto)
novoDicionario = dict()
resultado = 0
for l in dicionario.values():
    for t in l:
        for k,v in t.items():
            if k == 'quantidade':
                q = v
            if k == 'valor':
                resultado += v*q

print(resultado)