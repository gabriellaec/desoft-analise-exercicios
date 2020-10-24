import json
custo = 0
with open('estoque.json', 'r') as arquivo.json:
    texto = arquivo_json.read()
    dicionario = json.loads(texto)['dicionario']
# Transformando de volta para JSON (texto)
    for i in dicionario:
        quantidade = float(i['quantidade'])
        valor =  float(i['valor'])
        custo += quantidade*valor
        
print(custo)
        
